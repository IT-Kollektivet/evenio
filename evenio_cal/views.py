"""
Views for evenio
"""
from evenio_cal.models import Event, EventForm

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object

from django.core.serializers import serialize
from django.http import HttpResponse


def show_event(request, event_id):
    """ Show an event - wrapper arount object_detail 
    """

    events = Event.objects.all()

    if request.is_ajax():
        event = events.get(pk=event_id)
        json = serialize("json", event, use_natural_keys=True)
        return HttpResponse(json)
    else:
        return object_detail(request, events, object_id=event_id)


def list_events(request):
    """ List events
    """

    events = Event.objects.all()

    if request.is_ajax():
        json = serialize("json", events, use_natural_keys=True)
        return HttpResponse(json)
    else:
        return object_list(request, events)


def create_event(request):
    """ Creates an event
    """

    return create_object(request, Event, post_save_redirect="/kalender/")


def update_event(request, event_id):
    """ Updates an event
    """

    return update_object(request, Event, event_id, post_save_redirect="/kalender/")
