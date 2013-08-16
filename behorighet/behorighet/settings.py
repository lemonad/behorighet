"""
Django settings for behorighet project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!p9_7j2m_dkw3@kt8=m12ahqpgwh6!1-et)pvrrch)!g0s+6(*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.formtools',
    # 'django.contrib.markup',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    # Pip installed
    # 'debug_toolbar',
    # 'debug_toolbar_htmltidy',
    'south',
    # Local
    'criteria',
    'demo',
    'qualifications',
    'units',
    'users',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'behorighet.urls'

WSGI_APPLICATION = 'behorighet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'sv-SE'
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    )
TIME_ZONE = 'Europe/Stockholm'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Auth
AUTH_USER_MODEL = 'users.UserProfile'

# The below LOGIN_URL and LOGOUT_URL doesn't seem to be used
# except when unit testing views.
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

#
# Messages
#
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'alert-info',
                message_constants.INFO: 'alert-info',
                message_constants.WARNING: 'alert-warning',
                message_constants.ERROR: 'alert-error',
                message_constants.SUCCESS: 'alert-success'}

#
# debugging
#
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PANELS = (
    # 'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    # Removed due to it causing views to be called twice
    # 'debug_toolbar.panels.profiling.ProfilingDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar_htmltidy.panels.HTMLTidyDebugPanel',
    'haystack_panel.panel.HaystackDebugPanel',
)
