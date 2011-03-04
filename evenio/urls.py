from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    url(r'^$', 'evenio.views.list_events', name='list'),
    url(r'^search$', 'evenio.views.search', name='search'),
    url(r'^search/([\w-]+)$', 'evenio.views.search_events', name='search'),
    url(r'^events/([\w-]+)$', 'evenio.views.show_event', name='show'),
    url(r'^events/([\w-]+)/update$', 'evenio.views.update_event', name='update'),
    url(r'^create$', 'evenio.views.create_event', name='create'),
    # Lists for years, months and days are handled in a view.
    # Put this view lastly because it'll probably catch some unwanted URLs.
    url(r'^(\w+|\d+)(?:/(\w+|\d+))?$', 'evenio.views.list_events', name='list'),
)
