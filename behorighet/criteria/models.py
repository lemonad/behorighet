# -*- coding: utf-8 -*-
from django.conf import settings
from django.db.models import (CharField, DateTimeField, ForeignKey,
                              TextField, Manager, Model,
                              PositiveIntegerField)
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


class MetCriterionManager(Manager):
    pass


class MetCriterion(Model):
    BASES = \
        ((1, _('Formal education')),
         (2, _('Informal education')),
         (3, _('Test (summative)')),
         (4, _('Assessment (subjective)')),
         (99, _('Other')))

    user = ForeignKey(settings.AUTH_USER_MODEL,
                      verbose_name=_('user'))
    criterion = ForeignKey(Criterion,
                           verbose_name=_('criterion'))
    basis = PositiveIntegerField(_('basis'),
                                 db_index=True,
                                 choices=BASES)
    basis_description = TextField(_('basis description'),
                                  blank=True,
                                  default='')
    date_met = DateTimeField(_('date met'),
                             db_index=True)

    objects = MetCriterionManager()

    def __unicode__(self):
        return "%s met %s on %s" % (self.user.get_full_name(),
                                    self.criterion.name,
                                    self.date_met.date())

    class Meta:
        verbose_name = _('criterion')
        verbose_name_plural = _('criteria')
