# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import (CharField, DateTimeField, ForeignKey, Manager,
                              ManyToManyField, Model)
from django.utils.translation import ugettext_lazy as _

from qualifications.models import Qualification


class UnitManager(Manager):
    def qualifications_in_units(self, units):
        # TODO Union or intersection of qualifications?
        unit_ids = []
        for u in units:
            unit_ids.append(u.id)

        qualifications = Qualification.objects \
            .filter(unit__id__in=unit_ids)

        return qualifications


class Unit(Model):
    name = CharField(_('name'),
                     max_length=64,
                     unique=True,
                     db_index=True)
    # who has the right to see detailed data for this unit?
    owner = ForeignKey(settings.AUTH_USER_MODEL,
                       verbose_name=_('owner'),
                       related_name='owns_unit',
                       null=True,
                       blank=True)
    # which users belong to this unit?
    members = ManyToManyField(settings.AUTH_USER_MODEL,
                              verbose_name=_('members'),
                              related_name='units',
                              blank=True,
                              db_index=True)
    # which qualifications are relevant for this unit?
    qualifications = ManyToManyField(Qualification,
                                     verbose_name=_('qualifications'),
                                     related_name='units',
                                     blank=True,
                                     db_index=True)
    date_created = DateTimeField(_('created (date)'),
                                 null=False,
                                 db_index=True,
                                 auto_now_add=True)
    date_modified = DateTimeField(_('modified (date)'),
                                  null=False,
                                  db_index=True,
                                  auto_now=True)

    objects = UnitManager()

    def __unicode__(self):
        return self.name

    def per_qualification_statistics(self):
        """Qualification statistics on a unit level.

        Returns a list of...

        """
        # TODO Should be limited to the qualifications belonging to
        # TODO the unit?
        stats = []

        for q in self.qualifications.all():
            criteria_ids = q.criteria.values_list('id', flat=True)
            print self.members \
                .filter(met_criteria__id__in=criteria_ids) \
                .distinct()
            n_users_met_qualification = self.members \
                .filter(met_criteria__id__in=criteria_ids) \
                .distinct() \
                .count()
            stats.append((q, n_users_met_qualification))

        return stats

    def per_user_statistics(self):
        # TODO Should be limited to the qualifications belonging to
        # TODO the unit?
        pass

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')
