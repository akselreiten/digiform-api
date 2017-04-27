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
        #create sender
        self.user = create_user()

        #create receiver
        self.receiver = create_other_user()

        #create receiver
        self.university = create_university()

    def test_create_user_message(self):

        #defining message attributes
        data = {
            "sender":self.user.id,
            "receiver":self.receiver.id,
            "text":"morndu!",
        }

        self.url = reverse("chat-list-create") #getting url
        self.authorize_as_user(self.user) #authorize
        response = self.post(self.url,data) #posting
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data) #201 ok

    def test_unauth_create_university_review(self):
        data = {
            "sender":self.user.id,
            "receiver":self.receiver.id,
            "text":"morndu!",
        }

        self.url = reverse("chat-list-create")
        #not authorizing
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data) #not ok!

class GetUserMessageTest(ExtendedAPITestCase):

    #getting messages

    def setUp(self):
        self.user = create_user()

    def test_get_user_message(self):
        self.authorize_as_user(self.user)
        self.url = reverse("chat-list-create")
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_user_message(self):
        self.url = reverse("chat-list-create")
        #not authorized
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data) #not ok!