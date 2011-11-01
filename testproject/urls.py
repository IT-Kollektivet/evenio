from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from os import path as os_path

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('evenio_site.urls', namespace='evenio_site')),
    (r'^evenio/', include('evenio.urls', namespace='evenio')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),

    #(r'^media/(?P<path>.*)$', 'django.views.static.serve',
     #{'document_root': os_path.join(settings.SITE_ROOT, 'media'),
      #'show_indexes': True}),
    #(r'', include('evenio_site.urls',)),

)

urlpatterns += staticfiles_urlpatterns()
