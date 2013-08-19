# -*- coding: utf-8 -*-
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
