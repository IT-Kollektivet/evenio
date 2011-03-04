from django.db import models
from django.contrib.auth.models import User

# TODO:
# Events that repeat on different days are not modelled here.
# An Event should have a list of times when it occurs.
REPEAT_CHOICES = (
        ('n','None'),
        ('d','Daily'),
        ('w','Weekly'),
        ('m','Monthly'),
        ('y','Yearly'),
)

LANG_CHOICES = (
        ('da','Dansk'),
        ('en','English'),
)

class Category(models.Model):
    """ A category """
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def natural_key(self):
        return (self.id, self.title)


class Event(models.Model):
    """ A event """
    title = models.CharField(max_length=255) 
    starts = models.DateTimeField() # TODO: This should be a list of times!
    ends = models.DateTimeField(null=True, blank=True) # TODO: This should be a list of times!
    venue_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    category = models.ManyToManyField(Category)
    description = models.TextField()

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

    def __unicode__(self):
        return self.title


    class Meta:
        ordering = ('-starts',)
