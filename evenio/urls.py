from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    (r'^$', (lambda x: HttpResponse("Goodbye world!", status=404))),
    url(r'^list/$', 'evenio.views.list_events', name='list'),
    url(r'^event/(\d+)$', 'evenio.views.show_event', name='show'),
)
