from django.conf.urls.defaults import *
from django.http import Http404, HttpResponse

urlpatterns = patterns('',
    (r'^$', (lambda x: HttpResponse("Goodbye world!", status=404))),
)
