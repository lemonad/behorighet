# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'users.views',

    url(r'^(?P<username>.+?)/$',
        'user_profile',
        name="user-profile"),
)
