# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'units.views',

    url(r'^(?P<unitname>.+?)/$', 'unit', name="unit"),
)
