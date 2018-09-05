"""CBIBsite URL Configuration """
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

admin.site.site_header = 'CAIR admin'
admin.site.site_title = 'CAIR admin'
admin.site.site_url = 'http://cair.com/'
admin.site.index_title = 'CAIR administration'
admin.empty_value_display = '*Empty*'

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('nodes/', TemplateView.as_view(template_name='nodes.html'), name='node'),
    path('people/', TemplateView.as_view(template_name='people.html'), name='people'),
    path('admin/', admin.site.urls, name='admin'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    url(r'^', include('papers.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)