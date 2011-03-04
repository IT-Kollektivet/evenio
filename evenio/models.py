from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class Category(models.Model):
    """ A category """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=64)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('title',)

    def natural_key(self):
        return (self.id, self.title)


class Event(models.Model):
    """ A event """
    title = models.CharField(max_length=255) 
    slug = models.SlugField(max_length=64)
    
    starts = models.DateTimeField() # TODO: This should be a list of times!
    ends = models.DateTimeField(null=True, blank=True) # TODO: This should be a list of times!

    venue_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)

    categories = models.ManyToManyField(Category)
    
    description = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, null=True, blank=True)
    owner_anonymous = models.CharField(max_length=255, null=True, blank=True)

    price = models.IntegerField(null=True, blank=True)

    # Allow:
    rsvp = models.BooleanField(default=True)
    rsvp_anonymous = models.BooleanField(default=True)
    comments_before = models.BooleanField(default=True)
    comments_after = models.BooleanField(default=True)
    comments_anonymous_before = models.BooleanField(default=True)
    comments_anonymous_after = models.BooleanField(default=True)

    canceled = models.BooleanField(default=False)
    changed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-starts',)

    def get_categories_string(self):
        """Admin list"""
        return ", ".join([c.title for c in self.categories.all()])
    get_categories_string.short_description = _("Categories")
    
    