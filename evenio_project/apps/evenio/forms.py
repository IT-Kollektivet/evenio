from django.forms.models import ModelForm

from models import Event
from misc import make_custom_datefield

class EventForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Event
