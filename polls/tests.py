import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        returns False for questions whose pulish_date is in the future
        """
        time = timezone.now()+datetime.timedelta(days=30)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now()-datetime.timedelta(days=1, seconds=1)
        old_question = Question(publish_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now()-datetime.timedelta(hours=21, seconds=1)
        recent_question = Question(publish_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
