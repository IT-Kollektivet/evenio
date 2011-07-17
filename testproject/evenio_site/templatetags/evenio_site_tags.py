from django import template
register = template.Library()
from datetime import datetime
from evenio_site.forms import EvenioAuthenticationForm

from evenio.models import Category

def login_form(context):
    if context.get("login_form", False):
        return {'login_form': context.get("login_form")}
    return {
        'login_form': EvenioAuthenticationForm(initial={'redirect_to': context["request"].path})
    }
register.inclusion_tag('evenio_site/includes/login_form.html', takes_context=True)(login_form)

def category_list(context):
    filter_category = context.get("filter_category", None)
    filter_from = context.get("filter_from", None)
    if not filter_from:
        filter_from = datetime.now()
    return {
        'categories': Category.objects.all().order_by('title'),
        'filter_from': filter_from,
        'filter_category': filter_category,
    }
register.inclusion_tag('evenio_site/includes/category_list.html', takes_context=True)(category_list)
