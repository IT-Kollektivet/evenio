from django.conf.urls.defaults import *

urlpatterns = patterns('evenio_cal.views',
    (r'^$', 'list_events'),
    (r'^show/(?P<event_id>\d+)/$', 'show_event'),
    (r'^create/(?P<event_id>\d+)/$', 'create_event'),
    (r'^update/(?P<event_id>\d+)/$', 'update_event'),
)
