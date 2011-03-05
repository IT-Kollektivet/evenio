from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from os import path as os_path

from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^evenio/', include('evenio.urls', namespace='evenio')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': os_path.join(settings.SITE_ROOT, 'media'),
      'show_indexes': True}),
)
