# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


# Login
urlpatterns = patterns(
    'django.contrib',
    url(r'^$',
        'auth.views.login',
        {'template_name': 'login.html'},
        name="login"),
    url(r'^new-password/$',
        'auth.views.password_reset',
        {'template_name': 'password_reset_form.html',
         'email_template_name': 'password_reset_email.html'},
        name="password-reset"),
    url(r'^new-password/sent/$',
        'auth.views.password_reset_done',
        {'template_name': 'password_reset_done.html'},
        name="password-reset-done"),
    url(r'^new-password/complete/$',
        'auth.views.password_reset_complete',
        {'template_name': 'password_reset_complete.html'},
        name="password-reset-complete"),
    url(r'^new-password/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+?)/$',
        'auth.views.password_reset_confirm',
        {'template_name': 'password_reset_confirm.html'},
        name="password-reset-confirm"),
)
