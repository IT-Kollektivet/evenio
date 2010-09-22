"""
Views for evenio
"""
from evenio.models import Event

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object


def show_event(request, event_id):
    """ Show an event - wrapper arount object_detail 
        template: evenio/templates/evenio/event_detail.html
    """
    
    event = Event.objects.all()

    return object_detail(request, event, object_id=event_id)


def list_events(request):
    """ List events
        template: evenio/templates/evenio/event_list.html

        Needs a lot of work!
        Quite some arguments narrowing queryset
        down and stuff like that
    """
    
    events = Event.objects.all()

    return object_list(request, events)


def create_event(request):
    """ Creates an event
        template: evenio/templates/evenio/event_form.html
    """

    return create_object(request, Event)


def update_event(request, event_id):
    """ Updates an event
        template: evenio/templates/evenio/event_form.html
    """

    return update_object(request, Event, event_id)
