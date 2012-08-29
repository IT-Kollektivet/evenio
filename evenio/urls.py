from django.conf.urls.defaults import *
from views import EventUpdate
from views import EventDetail
from views import EventList
from views import EventCreate
from django.contrib.auth.decorators import login_required

from datetime import date
from models import Event

from django.views.generic import TodayArchiveView
from django.views.generic import WeekArchiveView
from django.views.generic import MonthArchiveView
from django.views.generic import YearArchiveView

urlpatterns = patterns('',
    url(r'^$', EventList.as_view(), name='list'),

    # Type based view
    url(r'^(?P<type>[\w-]+)/(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        EventList.as_view(),
        name='list_type'),

    # Datebased views

    url(r'^today',
        TodayArchiveView.as_view(model=Event, template_name='evenio/event_list.html',
            date_field='starts', allow_future=True, allow_empty=True)),

    url(r'^this-week',
        WeekArchiveView.as_view(model=Event, template_name='evenio/event_list.html',
        date_field='starts',
        week=date.today().strftime("%U"),
        year=date.today().strftime("%Y"),
        allow_future=True,
        allow_empty=True)),

    url(r'^this-month',
        MonthArchiveView.as_view(model=Event, template_name='evenio/event_list.html',
        date_field='starts',
        month=date.today().strftime("%b"),
        year=date.today().strftime("%Y"),
        allow_future=True,
        allow_empty=True)),

    url(r'^this-year',
        YearArchiveView.as_view(model=Event, template_name='evenio/event_list.html',
        date_field='starts',
        year=date.today().strftime("%Y"),
        allow_future=True,
        allow_empty=True)),

    # CRUD
    url(r'^events/(?P<slug>[\w-]+)$', EventDetail.as_view(), name='show'),
    url(r'^events/(?P<slug>[\w-]+)/update$', login_required(EventUpdate.as_view()), name='update'),
    url(r'^create$', login_required(EventCreate.as_view()), name='create'),


    #TODO: implement search
    #url(r'^search$', 'evenio.views.search_events', name='search'),
    #url(r'^search/([\w-]+)$', 'evenio.views.search_events', name='search'),
)
