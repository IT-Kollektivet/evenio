from django.contrib.auth.forms import AuthenticationForm
from django import forms

class EvenioAuthenticationForm(AuthenticationForm):
    redirect_to = forms.CharField(required=False, widget=forms.HiddenInput())