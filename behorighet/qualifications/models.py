# -*- coding: utf-8 -*-
from django.db.models import (CharField, DateTimeField, TextField, Manager,
                              ManyToManyField, Model)
from django.utils.translation import ugettext_lazy as _

from criteria.models import Criterion


class QualificationManager(Manager):
    def criteria_per_qualification(self):
        qualifications = super(QualificationManager, self) \
            .get_query_set().all()
        cpq = []
        for q in qualifications:
            criteria_ids = q.criteria \
                .values_list('id', flat=True) \
                .order_by('id')
            cpq.append((q.id, criteria_ids))
        return cpq


class Qualification(Model):
    name = CharField(_('name'),
                     max_length=64,
                     unique=True,
                     db_index=True)
    description = TextField(_('description'),
                            null=True,
                            blank=True,
                            default='')
    criteria = ManyToManyField(Criterion,
                               verbose_name=_('criterion'),
                               db_index=True)
    date_created = DateTimeField(_('created (date)'),
                                 null=False,
                                 db_index=True,
                                 auto_now_add=True)
    date_modified = DateTimeField(_('modified (date)'),
                                  null=False,
                                  db_index=True,
                                  auto_now=True)

    objects = QualificationManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('qualification')
        verbose_name_plural = _('qualifications')
