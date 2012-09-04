from eveniodk.models import NutGraf
from django.contrib import admin
from django.utils import html

# we define our resources to add to admin pages
class CommonMedia:
  js = (
    '//ajax.googleapis.com/ajax/libs/dojo/1.8.0/dojo/dojo.js',
    '/static/admin/js/editor.js',
  )
  css = {
    'all': ('/static/admin/css/editor.css',),
  }


class NutGrafAdmin(admin.ModelAdmin):
    list_display = ('heading', 'content_excerpt')
    
    '''
    formfield_overrides = {
        models.TextField: {'widget': RichTextEditorWidget},
    }
    '''
    
    def content_excerpt(self, obj):
        return html.strip_tags(obj.content)[:121]+"..."

admin.site.register(NutGraf, NutGrafAdmin, Media = CommonMedia,)