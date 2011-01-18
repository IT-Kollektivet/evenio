from django.conf.urls.defaults import *
from django.contrib import admin

from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views
from registration import views as reg_views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^kalender/', include('evenio_cal.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Comments
    (r'^comments/', include('django.contrib.comments.urls')),

    # Profiles
    (r'^profiles/', include('profiles.urls')),

    # Registration
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'registration/login.html'},
        name='auth_login'
    ),
    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'registration/logout.html'},
        name='auth_logout'
    ),
    url(r'^password/change/$',
        auth_views.password_change,
        name='auth_password_change'
    ),
    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='auth_password_change_done'
    ),
    url(r'^password/reset/$',
        auth_views.password_reset,
        name='auth_password_reset'
    ),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='auth_password_reset_confirm'
    ),
    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='auth_password_reset_complete'
    ),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='auth_password_reset_done'
    ),
    url(r'^register/$',
        reg_views.register,
        name='registration_register'
    ),
    url(r'^register/complete/$',
        direct_to_template,
        {'template': 'registration/registration_complete.html'},
        name='registration_complete'
    ),
)
