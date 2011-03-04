"""
Views for evenio
"""
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object

from django.core.serializers import serialize
from django.http import HttpResponse
import datetime

from models import Event

def show_event(request, event_id):
    """ Show an event - wrapper arount object_detail 
    """

    events = Event.objects.all()

    if request.is_ajax():
        event = events.get(pk=event_id)
        json = serialize("json", event, use_natural_keys=True)
        return HttpResponse(json)
    else:
        return object_detail(request,
                            events,
                            object_id=event_id,
                            template_object_name='event',
                            template_name='evenio/show_event.html',)


def list_events(request, year=None, month=None, day=None, max_results=0):
    """ List events
    """
    
    events = Event.objects.all()

    now = datetime.datetime.now()
    
    if not year:
        year = now.year
    if not month:
        month = now.month
    if not day:
        day = now.day
    
    events = events.filter(starts__gte=datetime.datetime(year=year, month=month, day=day),
                           starts__lte=datetime.datetime(year=year, month=month, day=31))

    if max_results > 0:
        events = events[:max_results]

    if request.is_ajax():
        json = serialize("json", events, use_natural_keys=True, 
                         fields=('title', 'starts', 'ends', 'price'))
        return HttpResponse(json)
    else:
        return object_list(request, events, template_name='evenio/list_events.html')


def create_event(request):
    """ Creates an event
    """

    return create_object(request, Event, template_name='evenio/create_event.html')


def update_event(request, event_id):
    """ Updates an event
    """

    return update_object(request, Event, event_id, template_name='evenio/update_event.html')
