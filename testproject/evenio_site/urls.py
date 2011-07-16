from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    url(r'^$', 'evenio_site.views.frontpage', name='frontpage'),
    url(r'^login-redirect/$', 'evenio_site.views.login_and_redirect', name='login_and_redirect'),
    url(r'^logout/$', 'evenio_site.views.logout', name='logout'),
)
