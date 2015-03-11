from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^addi/', include(admin.site.urls)),

    url(r'^api/location/', include('location.urls.api')),

    url(r'^$', 'location.views.index', name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
