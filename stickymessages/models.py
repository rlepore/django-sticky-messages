from django.utils import timezone

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class MessageManager(models.Manager):
    def get_all_active(self):
        """
        Get all of the active messages ordered by the active_datetime.
        """
        now = timezone.now()
        return self.select_related().filter(active_datetime__lte=now,
                                              inactive_datetime__gte=now).order_by('active_datetime')
    
    def get_latest_active(self):
        """
        Retrieve the latest active message, which is the message with the latest
        active_datetime
        """
        active = self.get_all_active()
        return list(active[:1])[0] if active else self.none()

class Message(models.Model):
    """
    Holds messages that will be displayed system wide.  We can use the active_datetime
    and the inactive_datetime to determine what active system message we would like to use.
    """
    message = models.TextField()
    active_datetime = models.DateTimeField(default=timezone.now)
    inactive_datetime = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, verbose_name=_('Created by'), null=True, blank=True,
                                   related_name="%(app_label)s_%(class)s_related_created")
    modified_by = models.ForeignKey(User, verbose_name=_('Modified by'), null=True, blank=True,
                                    related_name="%(app_label)s_%(class)s_related_modified")
    objects = MessageManager()