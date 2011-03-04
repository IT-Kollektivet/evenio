"""
Views for evenio
"""
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, update_object

from django.core.serializers import serialize
from django.http import HttpResponse
import datetime
import re

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


MONTHS = { # {{{
    'januar': 1,
    'january': 1,
    'jan': 1,
    '01': 1,

    'februar': 2,
    'february': 2,
    'feb': 2,
    '02': 2,

    'marts': 3,
    'march': 3,
    'mar': 3
    '03': 3,

    'april': 4,
    'apr': 4,
    '04': 4,

    'may': 5,
    'maj': 5,
    '05': 5,

    'juni': 6,
    'june': 6,
    'jun': 6,
    '06': 6,

    'juli': 7,
    'july': 7,
    'jul': 7,
    '07': 7,

    'august': 8,
    'aug': 8,
    '08': 8,

    'september': 9,
    'sep': 9,
    '09': 9,

    'oktober': 10,
    'october': 10,
    'oct': 10,
    'okt': 10,
    '10': 10,

    'november': 11,
    'nov': 11,
    '11': 11,
    
    'december': 12,
    'dec': 12,
    '12': 12,
} # }}}
def list_events(request, year=None, month=None, day=None):
    """ List events
    """

    max_results = request.GET.get('max_results', None)
    
    events = Event.objects.all()

    now = datetime.datetime.now()
    
    if not year:
        year = now.year

    month = MONTHS.get(month, None)
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

def search_events(request, search_string=None):
    """ Searches among events and produces a list of search results
    """

    max_results = request.GET.get('max_results', 10)

    events = Event.objects.all()

    query_string = request.GET.get("search_string", None)
    if query_string is None:
        if search_string is None or re.match(r'^\s*$', search_string):
            # Fejl -- intet søgeord
            pass

        for substr in re.split(r'-+', search_string):
            events = events.filter(__contains=substr)

    if max_results > 0:
        events = events[:max_results]

    return object_list(request, events, template_name='evenio/list_events.html')
