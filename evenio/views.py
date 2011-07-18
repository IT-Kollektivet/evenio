"""
Views for evenio
"""
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView


from django.core.serializers import serialize
from django.http import HttpResponse, Http404
import datetime
from datetime import timedelta
import re

import json

import evenio_settings

import forms
from models import Event
from forms import EventForm
from calendar import monthrange
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from evenio.models import Category


class EventDetail(DetailView):
    template_name = 'evenio/event_detail.html'
    context_object_name = 'event'

    def get_object(self):
        event = Event.objects.all().get(slug=self.kwargs['slug'])
        print self.kwargs['slug']

        if self.request.is_ajax():
            json = serialize("json", event, use_natural_keys=True)
            return HttpResponse(json)
        else:
            return event


class EventList(ListView):
    template_name = 'evenio/event_list.html'
    context_object_name = 'event_list'
    paginate_by = 10

    def get_queryset(self):
        events = Event.objects.all()
        now = datetime.datetime.now()

        kw_year = self.kwargs.get('year', None)
        kw_month = self.kwargs.get('month', None)
        kw_day = self.kwargs.get('day', None)
        kw_type = self.kwargs.get('type', None)
        max_results = self.kwargs.get('max_results', None)

        if not kw_year:
            year = now.year
        else:
            year = int(kw_year)

        try:
            month = int(kw_month)
        except TypeError:
            month = now.month
        if not month:
            month = now.month

        if not kw_day:
            # If no day is specified, we just return until the end of the month.
            if month == now.month:
                day = now.day
            else:
                day = 1
            until_day = monthrange(year, month)[1]
        else:
            day = int(kw_day)
            until_day = day

        # Out of range handling...
        if month > 12:
            raise Http404()
        if day > until_day:
            raise Http404()

        self.filter_from = datetime.datetime(year=year, month=month, day=day)

        events = Event.objects.all().filter(
                starts__gte=self.filter_from,
                starts__lte=datetime.datetime(year=year,
                    month=month,
                    day=until_day,
                    hour=23,
                    minute=59,
                    second=59)
                )

        if kw_type:
            self.category = get_object_or_404(Category, slug=kw_type)
            events = events.filter(categories=self.category)
        else:
            self.category = None
        events = events.order_by('starts')

        # If max results have been specified
        if max_results > 0:
            events = events[:max_results]

        if self.request.is_ajax():

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
            return events

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EventList, self).get_context_data(**kwargs)
        # Add in the publisher
        previous_month = self.filter_from.month - 1 if self.filter_from.month > 1 else 12
        previous_year = self.filter_from.year if previous_month < 12 else self.filter_from.year - 1
        next_month = self.filter_from.month + 1 if self.filter_from.month < 12 else 1
        next_year = self.filter_from.year if next_month > 1 else self.filter_from.year + 1
        context['filter_category'] = self.category
        context['filter_from'] = self.filter_from
        context['previous_month'] = datetime.date(month = previous_month, year = previous_year,
                                                  day = 1)
        context['next_month'] = datetime.date(month = next_month, year = next_year,
                                              day = 1)
        return context


class EventCreate(CreateView):
    """ Creates an event
    """

    form_class = EventForm
    model = Event
    template_name = 'evenio/event_create_form.html'
    context_object_name = 'event'

    # NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN!!!

class EventUpdate(UpdateView):
    """ Updates an event
    """

    form_class = EventForm
    model = Event
    template_name = 'evenio/event_update_form.html'
    context_object_name = 'event'

