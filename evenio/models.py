# coding:utf-8
'''
An calendar application
'''

from django.db import models
from django.contrib.auth.models import User

REPEAT_CHOICES = (
        ('d','Daily'),
        ('w','Weekly'),
        ('m','Monthly'),
        ('y','Yearly'),
)

LANG_CHOICES = (
        ('da','Dansk'),
        ('en','English'),
)


#TODO: There must be a better way of associating users and anonymous users
#to an event? The problem is that if the user is anonymous she should fill 
#out the name of the owner.

#User vs. anonymous problem:
#    Solution 1: Create a event without "owner" field and then two other models 
#                that inherit this model.
#    Solution 2: Have two fields "anonymous_owner" and "owner", and let the view
#                decide the representation.
#    Solution 3: Simply create a user when a anonymous creates an event.
#                Argument: the anonymous user probably wants to have the option
#                to adjust the event in case of errors or changes. 


class Event(models.Model):
    """ A event """
    title = models.CharField(max_length=255) 
    time = models.DateTimeField()
    repeat = models.CharField(max_length=1, choices=REPEAT_CHOICES)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    language = models.CharField(max_length=2, choices=LANG_CHOICES)
    description = models.TextField()

    # Allow:
    signup = models.BooleanField(default=True)
    comments = models.BooleanField(default=True)
    post_comments = models.BooleanField(default=True)
    anonymous_signup = models.BooleanField(default=True)
    anonymous_comments = models.BooleanField(default=True)
    anonymous_post_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class AnonymousEvent(Event):
    """ A anonymous event """

    owner = models.CharField(max_length=255)
    

class NormalEvent(Event):
    """ A normal event owned by an user """
    owner = models.ForeignKey(User) # User from auth framework


class Category(models.Model):
    """ A category """
    title = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.title


class EventProviderProfile(models.Model):
    """ A verified users profile """
    user = models.ForeignKey(User) # User from auth framework
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=75)
    website = models.URLField(verify_exists=False, max_length=200, blank=True,
                              null=True)
    description = models.TextField()

    def __unicode__(self):
        return self.name 
