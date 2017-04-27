from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from application.models import Application
from subjects.models import Subject
from digiform_api.utils.test_mixins import ExtendedAPITestCase
from digiform_api.utils.test_factory import create_user, create_foreign_subject, create_ntnu_subject
from views import AllApplicationsListCreateView
from django.urls import reverse
from rest_framework import status


class CreateApplicationTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.s1 = create_ntnu_subject()
        self.s2 = create_foreign_subject()

    def test_create_application(self):
        data = {
            "user":self.user.id,
            "ntnu_subject":self.s1.id,
            "replacing_subject":self.s2.id,
            "justification":"plz!",
            "application_status":"Processing"
        }

        self.url = reverse("application-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)

    def test_unauth_create_application(self):
        data = {
            "user":self.user.id,
            "ntnu_subject":self.s1.id,
            "replacing_subject":self.s2.id,
            "justification":"plz!",
            "application_status":"Accepted"
        }

        self.url = reverse("application-list-create")
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED, msg=response.data)

class GetApplicationTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_application(self):

        self.authorize_as_user(self.user)
        self.url = "/application/getApplications/?uni=&subject=&approval="
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_subject(self):
        self.url = "/application/getApplications/?uni=&subject=&approval="
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)


class GetSpecificApplicationTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.s1 = create_ntnu_subject()
        self.s2 = create_foreign_subject()
        self.uni_id = self.s2.university.id

        data = {
            "user":self.user.id,
            "ntnu_subject":self.s1.id,
            "replacing_subject":self.s2.id,
            "justification":"Strange justification for testing purposes",
            "application_status":"Processing"
        }

        self.url = reverse("application-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)

    def test_get_specific_application(self):

        self.authorize_as_user(self.user)
        self.url = "/application/getApplications/?uni=" + str(self.uni_id) + "&subject=&approval="
        response = self.get(self.url)
        self.assertEqual(response.data[0]["justification"],"Strange justification for testing purposes",msg=response.data)