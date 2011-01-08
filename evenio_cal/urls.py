from django.conf.urls.defaults import *

urlpatterns = patterns('evenio_cal.views',
    (r'^$', 'list'),
    (r'^show/(?P<event_id>\d+)/$', 'show'),
    (r'^create/(?P<event_id>\d+)/$', 'create'),
    (r'^update/(?P<event_id>\d+)/$', 'update'),
)
