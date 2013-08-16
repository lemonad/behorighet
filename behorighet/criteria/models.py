# -*- coding: utf-8 -*-
from django.db.models import (CharField, DateTimeField, TextField, Manager,
                              Model)
from django.utils.translation import ugettext_lazy as _


class CriterionManager(Manager):
    pass


class Criterion(Model):
    name = CharField(_('name'),
                     max_length=64,
                     unique=True,
                     db_index=True)
    description = TextField(_('description'),
                            null=True,
                            blank=True,
                            default='')
    date_created = DateTimeField(_('created (date)'),
                                 null=False,
                                 db_index=True,
                                 auto_now_add=True)
    date_modified = DateTimeField(_('modified (date)'),
                                  null=False,
                                  db_index=True,
                                  auto_now=True)

    objects = CriterionManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('criterion')
        verbose_name_plural = _('criteria')
