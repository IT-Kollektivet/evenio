from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from evenio import views

urlpatterns = patterns('',
    url(r'^$', views.EventsByDay.as_view(), name='list'),

    # Datebased views
    
    url(r'^today/(?P<type>)',
        views.EventsByCategory.as_view()),
    
    url(r'^today',
        views.EventsByDay.as_view()),

    url(r'^this-week',
        views.EventsByWeek.as_view()),

    url(r'^this-month',
        views.EventsByMonth.as_view()),

    url(r'^this-year',
        views.EventsByYear.as_view()),

    # CRUD
    url(r'^events/(?P<slug>[\w-]+)$', views.EventDetail.as_view(), name='show'),
    url(r'^events/(?P<slug>[\w-]+)/update$', login_required(views.EventUpdate.as_view()), name='update'),
    url(r'^create$', login_required(views.EventCreate.as_view()), name='create'),

)
