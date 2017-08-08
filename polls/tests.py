from django.test import TestCase
from django.utils import timezone
import datetime

from .models import Question

class QuestionMethodTest(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now()+datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)


	def test_was_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=3)
		recent_question = Question(pub_date=time)
		self.assertEqual(recent_question.was_published_recently(), True)


	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days=3)
		old_question = Question(pub_date = time)
		self.assertEqual(old_question.was_published_recently(), False)