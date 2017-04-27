from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from application.models import Application
from subjects.models import Subject
from digiform_api.utils.test_mixins import ExtendedAPITestCase
from digiform_api.utils.test_factory import create_user
from django.urls import reverse
from rest_framework import status


# Create your tests here.

class CreateUniversityTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()


    def test_create_university(self):
        data = {
            "title":"Test University",
            "city":"Test City",
            "country":"Test Country",
            "description":"Actually best university. Terrific stuff"
        }

        self.url = reverse("university-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED,msg=response.data)

    def test_unauth_create_university(self):
        data = {
            "title":"Test University",
            "city":"Test City",
            "country":"Test Country",
            "description":"Actually best university. Terrific stuff"
        }

        self.url = reverse("university-list-create")
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

class GetUniversityTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_any_university(self):
        self.authorize_as_user(self.user)
        self.url = "/universities/getUniversities/?title_contains=&city=&country=/"
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_university(self):
        self.url = "/universities/getUniversities/?title_contains=&city=&country=/"
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

