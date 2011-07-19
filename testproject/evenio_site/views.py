# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.views import login, logout as auth_logout
from django.utils.translation import ugettext_lazy as _

from evenio import views as evenio_views

import forms


def login_and_redirect(request):
    return login(request, template_name='login.html',
                 redirect_field_name='next',
                 authentication_form=forms.EvenioAuthenticationForm,
                 extra_context={'title': _(u"Log in")})


def logout(request):
    return auth_logout(request, next_page='/')


class Frontpage(evenio_views.EventList):
    template_name = 'frontpage.html'
