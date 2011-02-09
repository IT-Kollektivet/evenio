from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

urlpatterns = patterns('evenio_reg.views',
    (r'^register/$', 'register'),
    (r'^register/complete/$', 'register_complete'),

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'account/login.html'},
        name='auth_login'
    ),

    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'account/logout.html'},
        name='auth_logout'
    ),

    (r'^forgot/$', 'forgot_login'),
    (r'^forgot/confirmation-sent/$', 'confirmation_sent'),
    (r'^forgot/confirm/(?P<confirm_id>[0-9a-f]+)/$', 'confirm'),
)
