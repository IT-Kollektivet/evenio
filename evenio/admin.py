from django.contrib import admin

import models

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'starts', 'owner', 'get_categories_string', 'created')
    list_filter = ('categories',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Category, CategoryAdmin)