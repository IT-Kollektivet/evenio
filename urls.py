from django.conf.urls.defaults import *
from django.contrib import admin

from django.views.generic.simple import direct_to_template
from registration import views as reg_views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^kalender/', include('evenio_cal.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Profiles
    (r'^profiles/', include('profiles.urls')),

    # Registration
    (r'^account/', include('evenio_reg.urls')),
)
