"""
Views for evenio
"""
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object

from django.core.serializers import serialize
from django.http import HttpResponse, Http404
import datetime
import re

import json

import evenio_settings

import forms
from models import Event
from calendar import monthrange
from django.core.urlresolvers import reverse

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

    if not max_results:
        max_results = request.GET.get('max_results', 0)
    
    events = Event.objects.all()

    now = datetime.datetime.now()
    
    if not year:
        year = now.year
    else:
        year = int(year)

    try:
        month = int(month)
    except TypeError:
        month = evenio_settings.MONTH_SLUGS.get(month, None)
    if not month:
        month = now.month
    
    if not day:
        # If no day is specified, we just return until the end of the month.
        day = now.day
        until_day = monthrange(year, month)[1]
    else:
        day = int(day)
        until_day = day

    # Out of range handling...
    if month > 12:
        raise Http404()
    if day > until_day:
        raise Http404()
    
    events = events.filter(starts__gte=datetime.datetime(year=year, month=month, day=day),
                           starts__lte=datetime.datetime(year=year, month=month, day=until_day,
                                                         hour=23, minute=59, second=59) )

    # If max results have been specified
    if max_results > 0:
        events = events[:max_results]

    if request.is_ajax():
        
        # Put data explicitly in a dictionary instead of using
        # builtin Django functions
        events_dict = [{'title': event.title,
                        'starts': event.starts.isoformat(),
                        'ends': event.ends.isoformat() if event.ends else None,
                        'price': event.price,
                        'categories': [{'title': c.title, 'slug': c.slug} for c in event.categories.all()],
                        'show_url': reverse('evenio:show', args=(event.id,))} for event in events]
        
        data = json.dumps(events_dict,)
        return HttpResponse(data)
    else:
        return object_list(request, events, template_name='evenio/list_events.html')


def create_event(request):
    """ Creates an event
    """

    return create_object(request, Event, template_name='evenio/create_event.html',
                         form_class=forms.EventForm)


def update_event(request, event_id):
    """ Updates an event
    """

    return update_object(request, Event, event_id, template_name='evenio/update_event.html')

def search_events(request, search_string=None):
    """ Searches among events and produces a list of search results
    """

    max_results = request.GET.get('max_results', 10)

    events = Event.objects.all()

    query_string = request.GET.get("search_string", None)
    if query_string is None:
        if search_string is None or re.match(r'^\s*$', search_string):
            # Fejl -- intet
            pass

        for substr in re.split(r'-+', search_string):
            events = events.filter(__contains=substr)

    if max_results > 0:
        events = events[:max_results]

    return object_list(request, events, template_name='evenio/list_events.html')
