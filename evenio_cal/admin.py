from django.contrib import admin
from evenio_cal.models import Event

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
