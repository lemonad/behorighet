from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',)

urlpatterns += patterns(
    'main.views',

    # Startpage
    url(r'^$', 'startpage', name="startpage"),
)

urlpatterns += patterns(
    '',
    (r'^criteria/', include('criteria.urls')),
    (r'^login/', include('login.urls')),
    (r'^qualifications/', include('qualifications.urls')),
    (r'^units/', include('units.urls')),
    (r'^users/', include('users.urls')),

    (r'^admin/', include(admin.site.urls)),
)

# Logout
urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^logout/$',
        'logout',
        {'template_name': 'logout.html'},
        name="logout"),
)

urlpatterns += patterns(
    '',
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
