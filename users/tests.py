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
        #create user
        self.user = create_user()

    def test_create_user(self):
        data = {
            "username":"martins",
            "email":"martinsommmer@mail.com",
            "password":"santab",
            "first_name":"Martin",
            "last_name":"Sommerseth",
        }

        self.url = "/users/createUser/" #url for creating user
        self.authorize_as_user(self.user) #authorize
        response = self.post(self.url,data) #create user
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data) #200 created

    def test_unauth_create_user(self):

        #trying to create user without being logged in

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
        #201 ok!
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
            #get attribute error because it makes no sense
            #trying to get your own user when not logged in
            pass