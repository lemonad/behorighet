# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, DateTimeField, TextField, Manager,
                              ManyToManyField, Model)
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


class MyUser(AbstractUser):
    avatar = ThumbnailerImageField(_('avatar'),
                                   upload_to='avatars',
                                   null=True,
                                   blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('qualification')
        verbose_name_plural = _('qualifications')
