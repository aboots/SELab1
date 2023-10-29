from django.test import TestCase

# Create your tests here. write test for me
from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
import datetime
from .models import MemoUser
# Create your tests here.

class MemoUserModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future. 
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = MemoUser(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
         was_published_recently() returns False for questions whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = MemoUser(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
         was_published_recently() returns True for questions whose pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = MemoUser(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_user(username, password, email):
    """
    Create a user with the given `username`, `password` and `email`.
    """
    return MemoUser.objects.create(username=username, password=password, email=email, pub_date=timezone.now()

class MemoUserIndexViewTests(TestCase):
    def test_no_users(self):
        """
        If no users exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('memo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No users are available.")
        self.assertQuerysetEqual(response.context['latest_user_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_user(username="Past user.", password="123456", email="example@gmail.com", pub_date=timezone.now() - datetime.timedelta(days=30))
        response = self.client.get(reverse('memo:index'))
        self.assertQuerysetEqual(
            response.context['latest_user_list'],
            ['<MemoUser: Past user.>']
        )

