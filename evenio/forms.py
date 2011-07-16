from django.forms.models import ModelForm

from models import Event

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('slug','owner','owner_anonymous')
