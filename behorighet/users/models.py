# -*- coding: utf-8 -*-
import os

from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Manager, ManyToManyField
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from criteria.models import Criterion, MetCriterion
from qualifications.models import Qualification


class UserUnitManager(Manager):
    def users_in_units(self, units):
        unit_ids = []
        for u in units:
            unit_ids.append(u.id)

        users = super(UserUnitManager, self) \
            .get_query_set() \
            .filter(unit__id__in=unit_ids)

        return users


class UserProfile(AbstractUser):
    avatar = ThumbnailerImageField(_('avatar'),
                                   upload_to='avatars',
                                   null=True,
                                   blank=True)
    met_criteria = ManyToManyField(Criterion,
                                   through=MetCriterion,
                                   verbose_name=_('met criteria'),
                                   related_name='users_met',
                                   blank=True,
                                   db_index=True)

    objects = UserManager()
    unit_related = UserUnitManager()

    def __unicode__(self):
        return "%s (%s)" % (self.get_full_name(), self.username)

    def _criteria_ids_met(self):
        """Returns a list of ids of the criteria the user has met."""
        return self.met_criteria.values_list('id', flat=True)

    def has_met_qualifications(self, qualifications):
        """Has the user met the given qualifications?

        Returns True if all given qualifications has been met

        """
        criteria_met = self._criteria_ids_met()

        qualification_ids = []
        for q in qualifications:
            qualification_ids.append(q.id)

        criteria = Criterion.objects \
            .filter(qualification__id__in=qualification_ids) \
            .values_list('id', flat=True)

        return set(criteria).issuperset(set(criteria_met))

    def qualifications(self):
        """Which qualifications has the user met?

        Returns a list of qualification query objects.

        """
        # TODO Should be limited to the qualifications belonging to
        # TODO the user's units?

        criteria_met = self._criteria_ids_met()

        potential_qualifications = Qualification.objects \
            .filter(criteria__in=criteria_met)

        qualifications_met = []
        for pq in potential_qualifications:
            pqc = pq.criteria.values_list('id', flat=True)
            if set(pqc).issubset(set(criteria_met)):
                qualifications_met.append(pq.id)

        q = Qualification.objects.filter(id__in=qualifications_met)
        return q

    def qualifications_not_met(self):
        """Which qualifications (in his/her units) has the user not met?

        Returns a list of qualification query objects limited by
        the qualifications in the unit the user belongs to.

        """
        qualifications_met = self.qualifications().values_list('id', flat=True)
        user_units = self.units.values_list('id', flat=True)

        qnm = Qualification.objects \
            .exclude(id__in=qualifications_met) \
            .filter(units__in=user_units)

        return qnm

    def qualification_criteria(self, qualification):
        """ Given a specific qualification, which criteria
        has the user met and not met?

        Returns a tuple of met criteria and not met criteria
        lists, each list item a tuple of (criterion, metcriterion),
        if the criterion is met, or (criterion, None) if not met.

        """
        criteria_met = []
        criteria_not_met = []
        for c in qualification.criteria.all():
            try:
                mc = MetCriterion.objects \
                    .filter(user__id=self.id) \
                    .filter(criterion__id=c.id) \
                    .get()
                criteria_met.append((c, mc))
            except MetCriterion.DoesNotExist:
                criteria_not_met.append((c, None))
        return (criteria_met, criteria_not_met)

    def get_avatar(self):
        if self.avatar:
            return self.avatar
        else:
            return "avatars/default.jpg"

    def get_avatar_path(self):
        if self.avatar:
            return self.avatar.path
        else:
            return os.path.join(settings.STATIC_ROOT,
                                "avatars/default.jpg")

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return settings.STATIC_URL + "avatars/default.jpg"
