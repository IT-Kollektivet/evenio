"""
Views for evenio
"""
from evenio_cal.models import Event

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object

from django.core.serializers import serialize
from django.http import HttpResponse


def show_event(request, event_id):
    """ Show an event - wrapper arount object_detail 
        template: evenio/templates/event_detail.html
    """

    events = Event.objects.all()

    if request.is_ajax():
        json = serialize("json", events, use_natural_keys=True)
        return HttpResponse(json)
    else:
        return object_detail(request, events, object_id=event_id)


def list_events(request):
    """ List events
        template: evenio/templates/event_list.html
    """

    events = Event.objects.all()

    return object_list(request, events)


def create_event(request):
    """ Creates an event
        template: evenio/templates/event_form.html
    """

    return create_object(request, Event)


def update_event(request, event_id):
    """ Updates an event
        template: evenio/templates/event_form.html
    """

    return update_object(request, Event, event_id)
