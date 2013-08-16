# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import (CharField, DateTimeField, ForeignKey, Manager,
                              ManyToManyField, Model)
from django.utils.translation import ugettext_lazy as _

from qualifications.models import Qualification


class UnitManager(Manager):
    pass


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

    class Meta:
        verbose_name = _('unit')
        verbose_name_plural = _('units')
