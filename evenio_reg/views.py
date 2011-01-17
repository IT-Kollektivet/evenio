from django import forms
from models import EvenioUserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = EvenioUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # TODO: Auto log-in
            return HttpResponseRedirect("/register/complete/")
        else:
            context = {
                'form': EvenioUserCreationForm(),
            }
            context.update(csrf(request))
            return render_to_response("register.html", context)
    else:
        context = {
            'form': EvenioUserCreationForm(),
        }
        context.update(csrf(request))
        return render_to_response("register.html", context)

@login_required
def register_complete(request):
    return render_to_response("register_complete.html")

def forgot_login(request):
    pass

def confirmation_sent(request):
    pass

def confirm(request, confirm_id):
    pass
