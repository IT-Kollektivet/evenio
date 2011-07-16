from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    url(r'^$', 'evenio_site.views.frontpage', name='frontpage'),
)
