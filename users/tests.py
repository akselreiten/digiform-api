from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from application.models import Application
from subjects.models import Subject
from digiform_api.utils.test_mixins import ExtendedAPITestCase
from digiform_api.utils.test_factory import create_user, create_university, create_other_user
from django.urls import reverse
from rest_framework import status


# Create your tests here.

class CreateUserTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.receiver = create_other_user()
        self.university = create_university()

    def test_create_user(self):
        data = {
            "username":"martins",
            "email":"martinsommmer@mail.com",
            "password":"santab",
            "first_name":"Martin",
            "last_name":"Sommerseth",
        }

        self.url = "/users/createUser/"
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)

    def test_unauth_create_user(self):

        data = {
            "username":"martins",
            "email":"martinsommmer@mail.com",
            "password":"santab",
            "first_name":"Martin",
            "last_name":"Sommerseth",
        }

        self.url = reverse("current-user")
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)
        #user doesn't have to be logged in to create user

class GetUserTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_user(self):
        self.authorize_as_user(self.user)
        self.url = reverse("get-user")
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_user(self):
        self.url = reverse("get-user")
        try:
            response = self.get(self.url)
        except AttributeError:
            pass