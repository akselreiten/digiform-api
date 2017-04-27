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

        #university attributes
        data = {
            "title":"Test University",
            "city":"Test City",
            "country":"Test Country",
            "description":"Actually best university. Terrific stuff"
        }

        self.url = reverse("university-list-create") #get url
        self.authorize_as_user(self.user) #authorize
        response = self.post(self.url,data) #create
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED,msg=response.data)
        #405?
        #user cannot create new university
        #only admin can from backend

    def test_unauth_create_university(self):
        data = {
            "title":"Test University",
            "city":"Test City",
            "country":"Test Country",
            "description":"Actually best university. Terrific stuff"
        }

        self.url = reverse("university-list-create")
        response = self.post(self.url,data)
        #not authorized
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data) # 401 ok

class GetUniversityTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_any_university(self):
        self.authorize_as_user(self.user)
        self.url = "/universities/getUniversities/?title_contains=&city=&country=/" #filtering in all universities
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_university(self):
        #not authorized
        self.url = "/universities/getUniversities/?title_contains=&city=&country=/"
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

