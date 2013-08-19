# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import Manager, ManyToManyField
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from criteria.models import Criterion, MetCriterion
from qualifications.models import Qualification


class UserQualificationsManager(Manager):
    pass


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
    qualification_objects = UserQualificationsManager()

    def qualifications(self):
        # TODO Should be limited to the qualifications belonging to
        # TODO the user's units?
        # units = self.units_set.all()
        # print units

        criterias_met = self.met_criteria.values_list('id', flat=True)

        potential_qualifications = Qualification.objects.filter(criteria__in=criterias_met)
        for pq in potential_qualifications:
            pqc = pq.criteria.values_list('id', flat=True)
            TODO xyz


        qualifications = []
        qualifications = qualifications.all()

            for uq in unit_qualifications:
                uqc = uq.criteria.all()




        qualifications = Qualification
