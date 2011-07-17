from django.forms.models import ModelForm

from models import Event
from misc import make_custom_datefield

class EventForm(ModelForm):
    formfield_callback = make_custom_datefield
    class Meta:
        model = Event
        exclude = ('slug','owner','owner_anonymous', 'comments_before',
                'comments_after', 'comments_anonymous_before',
                'comments_anonymous_after', 'rsvp', 'rsvp_anonymous',
                'canceled', 'changed')
