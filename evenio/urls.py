from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    (r'^$', (lambda x: HttpResponse("Goodbye world!", status=404))),
    url(r'^search$', 'evenio.views.search', name='search'),
    url(r'^search/([\w-]+)$', 'evenio.views.search_events', name='search'),
    url(r'^events/([\w-]+)$', 'evenio.views.show_event', name='show'),
    url(r'^events/([\w-]+)/update$', 'evenio.views.update_event', name='update'),
    url(r'^create$', 'evenio.views.create_event', name='create'),
)
