from django.db import models
from django.contrib.auth.models import User
from django.contrib.comments.models import Comment
from django.contrib.comments.signals import comment_was_flagged
from django.utils.translation import ugettext_lazy as _

from django.core.urlresolvers import reverse

from django.template.defaultfilters import slugify
from misc import slugify_uniquely
from misc import AutoSlugField


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
    """ An event """

    title = models.CharField(max_length=255,
        verbose_name=_("Title"),
        help_text=_("The title of the event"))
    slug = models.SlugField(max_length=64, unique=True,
        verbose_name=_("Slug"),
        help_text=_("A unique identifier based on the title"))

    # TODO: These should be lists of times!
    starts = models.DateTimeField(null=False, blank=False,
        verbose_name=_("Starts"),
        help_text=_("When the event begins"))
    ends = models.DateTimeField(null=True, blank=True,
        verbose_name=_("Ends"),
        help_text=_("When the event ends"))

    venue_name = models.CharField(max_length=255,
        verbose_name=_("Venue"),
        help_text=_("The name of the place where the event is held"))

    address = models.CharField(max_length=255, null=True, blank=True,
        verbose_name=_("Address"),
        help_text=_("The address for the place where the event is held"))

    categories = models.ManyToManyField(Category,
        verbose_name=_("Categories"),
        help_text=_("The type of event"))

    description = models.TextField(blank=True,
        verbose_name=_("Description")) # TODO: help_text=_("")

    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Created"))
    changed = models.DateTimeField(auto_now=True, verbose_name=_("Changed"))

    owner = models.ForeignKey(User, null=True, blank=True,
        verbose_name=_("Owner"))
    owner_anonymous = models.CharField(max_length=255, null=True, blank=True,
        verbose_name=_("Owner (anonymous)"))

    price = models.IntegerField(null=True, blank=True,
        verbose_name=_("Price"),
        help_text=_("The cost for participating. Be kind to note in the " +
                    "description of the event if people have to sign up, " +
                    "and how this is done, before they can participate."))

    # Allow:
    rsvp = models.BooleanField(default=True, verbose_name=_("RSVP"),
        help_text=_("Do participants have to say whether they will attend " +
                    "to be allowed to attend?"))
    rsvp_anonymous = models.BooleanField(default=True,
        verbose_name=_("RSVP (anonymous)"),
        help_text=_("Can people say that they attend even when they are not " +
                    "logged in?"))
    comments_before = models.BooleanField(default=True,
        verbose_name=_("Comments before event"),
        help_text=_("Can people post comments before the event?"))
    comments_after = models.BooleanField(default=True,
        verbose_name=_("Comments after event"),
        help_text=_("Can people post comments after the event?"))
    comments_anonymous_before = models.BooleanField(default=True,
        verbose_name=_("Comments (anonymous) before event"),
        help_text=_("Can people post comments anonymously before the event?"))
    comments_anonymous_after = models.BooleanField(default=True,
        verbose_name=_("Comments (anonymous) after event"),
        help_text=_("Can people post comments anonymously after the event?"))

    # FIXME: cancelled
    canceled = models.BooleanField(default=False, verbose_name=_("Cancelled"))
    changed = models.BooleanField(default=False, verbose_name=_("Changed"))


    def __unicode__(self):
        return self.title


    class Meta:
        ordering = ('-starts',)


    def get_absolute_url(self):
        return reverse('evenio:show', kwargs={'slug':self.slug})


    def get_categories_string(self):
        """Admin list"""
        return ", ".join([c.title for c in self.categories.all()])


    def save(self, *args, **kwargs):
        self.slug = slugify_uniquely(self.title, Event)
        super(Event, self).save(*args, **kwargs)


    get_categories_string.short_description = _("Categories")


class FlaggedComment(models.Model):
    """
    A (dirty hack?) way to register flagged comments
    """
    comment = models.ForeignKey(Comment)

    def __unicode__(self):
        return self.comment.user_name + ': ' + self.comment.comment


def on_comment_was_flagged(sender, comment, request, flag, *args, **kwargs):
    flagged = FlaggedComment(comment=comment)
    flagged.save()

    print comment.id

comment_was_flagged.connect(on_comment_was_flagged)




### GENERATE TEST DATA ###

def generate_test_data():
    from datetime import datetime, timedelta
    from random import choice, randint
    dates = 300
    now = datetime.now()

    categories = ["Food", "Concert", "Party", "Talk", "Poetry"]

    names = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
    names = slugify(names).split("-")

    for c in categories:
        cat = Category(title=c, slug=slugify(c))
        cat.save()

    categories = Category.objects.all()

    for _ in range(1000):

        e = Event()
        e.title = "%s %s" % (choice(names), choice(names))
        e.title = e.title[0].upper() + e.title[1:]
        e.slug = slugify(e.title)
        e.starts = now + timedelta(days=randint(0, dates))
        e.price = choice([0,100,200,20,30,50])
        e.description = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
        e.save()
        for c in categories.order_by('?')[:randint(1,3)]:
            e.categories.add(c)
