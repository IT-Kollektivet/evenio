from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class EvenioUserCreationForm(UserCreationForm):
    username = forms.RegexField(max_length=60, regex=r'^.+@.+$',
            label = _("Email"),
            help_text = _("Must contain a valid email address."),
            error_messages = {
                'invalid': _("Must contain a valid email address."),
            })
