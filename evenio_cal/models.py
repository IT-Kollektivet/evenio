# coding:utf-8
'''
An calendar application
'''

from django.db import models
from django.contrib.auth.models import User

from django.forms import ModelForm

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
    happens = models.DateTimeField()
    repeat = models.CharField(max_length=1, choices=REPEAT_CHOICES, default='n')
    address = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    language = models.CharField(max_length=2, choices=LANG_CHOICES, default='da')
    short_description = models.CharField(max_length=140)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, null=True, blank=True)
    owner_anonymous = models.CharField(max_length=255, null=True, blank=True)

    # Allow:
    signup = models.BooleanField(default=True)
    comments_before = models.BooleanField(default=True)
    comments_after = models.BooleanField(default=True)
    signup_anonymous = models.BooleanField(default=True)
    comments_anonymous_before = models.BooleanField(default=True)
    comments_anonymous_after = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class EventForm(ModelForm):
    class Meta:
        model = Event

class UserProfile(models.Model):
    """ A verified users profile """
    user = models.ForeignKey(User) # User from auth framework
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=75)
    website = models.URLField(verify_exists=False, max_length=200, blank=True,
                              null=True)
    description = models.TextField()
    verified = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })

    get_absolute_url = models.permalink(get_absolute_url)
