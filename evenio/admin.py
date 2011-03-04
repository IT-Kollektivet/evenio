from django.contrib import admin

import models

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Event, EventAdmin)
