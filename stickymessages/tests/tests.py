from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from stickymessages import models

class MessageModelTests(TestCase):
    fixtures = ['test_data']
    
    def test_inactive_message(self):
        from django.db.models.query import EmptyQuerySet
        self.assertIsInstance(models.Message.objects.get_latest_active(), EmptyQuerySet)
        
    def test_active_message(self):
        ##Add an active message to the database, can't do this in the fixture
        ##since the date can not be static.
        message = models.Message(message = 'This is an active message.',
                                 active_datetime = timezone.now(),
                                 inactive_datetime = timezone.now() + timedelta(days=1))

        message.save()
        active_message = models.Message.objects.get_latest_active()
        self.assertIsInstance(active_message, models.Message)
        self.assertEquals(active_message.message, 'This is an active message.')