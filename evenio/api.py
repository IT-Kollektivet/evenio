from tastypie.resources import ModelResource
from tastypie import fields
from models import Category, Event


class CategoryResource(ModelResource):
        
    class Meta:
        queryset = Category.objects.all()


class EventResource(ModelResource):
    categories = fields.ToManyField('evenio.api.CategoryResource', 'categories')
    
    class Meta:
        queryset = Event.objects.all()    