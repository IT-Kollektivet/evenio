"""
Views for evenio
"""
from evenio_cal.models import Event, EventForm

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object


def show_event(request, event_id):
    """ Show an event - wrapper arount object_detail 
    """

    event = Event.objects.all()

    return object_detail(request, event, object_id=event_id)


def list_events(request):
    """ List events
    """

    events = Event.objects.all()

    return object_list(request, events)


def create_event(request):
    """ Creates an event
    """

    return create_object(request, Event, post_save_redirect="/evenio/")


def update_event(request, event_id):
    """ Updates an event
    """

    return update_object(request, Event, event_id)
