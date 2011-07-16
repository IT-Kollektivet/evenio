from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

import views

urlpatterns = patterns('',
    url(r'^$', views.Frontpage.as_view(), name='frontpage'),
    url(r'^login-redirect/$', 'evenio_site.views.login_and_redirect', name='login_and_redirect'),
    url(r'^logout/$', 'evenio_site.views.logout', name='logout'),
)
