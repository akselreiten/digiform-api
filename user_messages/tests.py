from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from application.models import Application
from subjects.models import Subject
from digiform_api.utils.test_mixins import ExtendedAPITestCase
from digiform_api.utils.test_factory import create_user, create_university, create_other_user
from django.urls import reverse
from rest_framework import status


# Create your tests here.

class CreateUserMessageTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.receiver = create_other_user()
        self.university = create_university()

    def test_create_user_message(self):
        data = {
            "sender":self.user.id,
            "receiver":self.receiver.id,
            "text":"morndu!",
        }

        self.url = reverse("chat-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)

    def test_unauth_create_university_review(self):
        data = {
            "sender":self.user.id,
            "receiver":self.receiver.id,
            "text":"morndu!",
        }

        self.url = reverse("chat-list-create")
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

class GetUniversityReviewTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_user_message(self):
        self.authorize_as_user(self.user)
        self.url = reverse("chat-list-create")
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_user_message(self):
        self.url = reverse("chat-list-create")
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)