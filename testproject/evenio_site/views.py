# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.views import auth_login
from django.contrib.auth import login

import forms

def login_and_redirect(request):
    if request.method == 'POST':
        form = forms.EvenioAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(user)
            redirect_to = form.cleaned_data["redirect_to"]
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('frontpage')
        else:
            print form.errors
    else:
        form = forms.EvenioAuthenticationForm()
    context = RequestContext(request, {'login_form': form})
    return render_to_response("login.html", context)

def frontpage(request):
    
    context = RequestContext(request)
    return render_to_response("frontpage.html", context)
    