# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.views import login, logout as auth_logout
from django.utils.translation import ugettext_lazy as _

import forms

def login_and_redirect(request):
    return login(request, template_name='login.html',
                 redirect_field_name='next',
                 authentication_form=forms.EvenioAuthenticationForm,
                 extra_context={'title': _(u"Log ind")})

def logout(request):
    return auth_logout(request, next_page='/')

def frontpage(request):
    
    context = RequestContext(request, {'title': _(u"Frontpage")})
    return render_to_response("frontpage.html", context)
    