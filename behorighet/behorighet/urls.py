from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^criteria/', include('criteria.urls')),
    (r'^qualifications/', include('qualifications.urls')),
    (r'^units/', include('units.urls')),
    (r'^users/', include('users.urls')),

    (r'^admin/', include(admin.site.urls)),
)
