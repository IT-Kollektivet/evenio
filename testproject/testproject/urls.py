from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

from tastypie.api import Api
from evenio.api import CategoryResource, EventResource

v1_api = Api(api_name="v1")
v1_api.register(CategoryResource())
v1_api.register(EventResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('evenio.urls', namespace='evenio')),

)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
