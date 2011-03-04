from django.contrib import admin

import models

class EventAdmin(admin.ModelAdmin):
    list_display = ('starts', 'title', 'get_categories_string')
    list_filter = ('categories',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Category)