from django import template
register = template.Library()

from evenio_site.forms import EvenioAuthenticationForm

def login_form(context):
    if context.get("login_form", False):
        return {'login_form': context.get("login_form")}
    return {
        'login_form': EvenioAuthenticationForm(initial={'redirect_to': context["request"].path})
    }
register.inclusion_tag('evenio_site/includes/login_form.html', takes_context=True)(login_form)
