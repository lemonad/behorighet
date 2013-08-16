# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import ManyToManyField
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField

from criteria.models import Criterion, MetCriterion


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
