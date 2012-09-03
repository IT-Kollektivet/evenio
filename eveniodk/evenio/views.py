"""
Views for evenio
"""
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView
from evenio.models import Category
from forms import EventForm
from models import Event
from django.views.generic.dates import TodayArchiveView, WeekArchiveView,\
    MonthArchiveView, YearArchiveView
from datetime import date

class EventDetail(DetailView):
    template_name = 'evenio/event_detail.html'
    context_object_name = 'event'
    model = Event


class CategoryTypeMixin():
    def get_queryset(self):
        qs = super(CategoryTypeMixin, self).get_queryset()
        kw_type = self.kwargs.get('type', None)
        if kw_type:
            self.category = get_object_or_404(Category, slug=kw_type)
            qs = qs.filter(categories=self.category)
        return qs

class EventsByCategory(TodayArchiveView, CategoryTypeMixin):
    """Takes an additional url kw argument 'type'"""
    model=Event
    template_name='evenio/event_list.html'
    date_field='starts'
    allow_future=True
    allow_empty=True

class EventsByDay(TodayArchiveView):
    model=Event
    template_name='evenio/event_list.html'
    date_field='starts'
    allow_future=True
    allow_empty=True

class EventsByWeek(WeekArchiveView):
    model=Event
    template_name='evenio/event_list.html'
    date_field='starts'
    allow_future=True
    allow_empty=True
    
    def get_year(self):
        return date.today().strftime("%Y")
    
    def get_week(self):
        return date.today().strftime("%U")
    
class EventsByMonth(MonthArchiveView):
    model=Event
    template_name='evenio/event_list.html'
    date_field='starts'
    allow_future=True
    allow_empty=True
    
    def get_year(self):
        return date.today().strftime("%Y")
    
    def get_month(self):
        return date.today().strftime("%b")

class EventsByYear(YearArchiveView):
    model=Event
    template_name='evenio/event_list.html'
    date_field='starts'
    allow_future=True
    allow_empty=True
    
    def get_year(self):
        return date.today().strftime("%Y")
    
class EventCreate(CreateView):
    """ Creates an event
    """

    form_class = EventForm
    model = Event
    template_name = 'evenio/event_form.html'
    context_object_name = 'event'

    # NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN NYAN!!!

class EventUpdate(UpdateView):
    """ Updates an event
    """

    form_class = EventForm
    model = Event
    template_name = 'evenio/event_form.html'
    context_object_name = 'event'

