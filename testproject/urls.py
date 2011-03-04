from django.conf.urls.defaults import *
from django.contrib import admin

from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    (r'^evenio/', include('evenio.urls', namespace='evenio')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),
)
