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
        self.user = create_user() #creating test user
        self.s1 = create_ntnu_subject() #creating test ntnu subject
        self.s2 = create_foreign_subject() #creating test foreign subject

    def test_create_application(self):

        #defining application data
        data = {
            "user":self.user.id,
            "ntnu_subject":self.s1.id,
            "replacing_subject":self.s2.id,
            "justification":"plz!",
            "application_status":"Processing"
        }

        #creating url
        self.url = reverse("application-list-create")

        #authorizing user
        self.authorize_as_user(self.user)

        #retrieving response
        response = self.post(self.url,data)

        #expecting HTTP 201 Created
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)

    def test_unauth_create_application(self):

        #defining application data
        data = {
            "user":self.user.id,
            "ntnu_subject":self.s1.id,
            "replacing_subject":self.s2.id,
            "justification":"plz!",
            "application_status":"Accepted"
        }

        #creating url
        self.url = reverse("application-list-create")

        #not authorizing user

        #retrieving response
        response = self.post(self.url,data)

        #expecting HTTP 401 Unauthorized
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED, msg=response.data)

class GetApplicationTest(ExtendedAPITestCase):

    #test user
    def setUp(self):
        self.user = create_user()


    #getting application
    def test_get_application(self):

        #authorizing
        self.authorize_as_user(self.user)

        #selecting all applications
        self.url = "/application/getApplications/?uni=&subject=&approval="

        #getting response
        response = self.get(self.url)

        #expecting 200 OK
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_subject(self):

        #same procedure without authentication
        self.url = "/application/getApplications/?uni=&subject=&approval="
        response = self.get(self.url)

        #expecting http 401 unauthorized
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)


class GetSpecificApplicationTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.s1 = create_ntnu_subject()
        self.s2 = create_foreign_subject()
        self.uni_id = self.s2.university.id


        #defining test application
        data = {
            "user":self.user.id,
            "ntnu_subject":self.s1.id,
            "replacing_subject":self.s2.id,
            "justification":"Strange justification for testing purposes",
            "application_status":"Processing"
        }

        #inserting test application into test database

        self.url = reverse("application-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)

    def test_get_specific_application(self):

        #retrieving the test application

        self.authorize_as_user(self.user)

        #using university id as identification
        self.url = "/application/getApplications/?uni=" + str(self.uni_id) + "&subject=&approval="
        response = self.get(self.url)

        #asserting that justification is equal
        self.assertEqual(response.data[0]["justification"],"Strange justification for testing purposes",msg=response.data)

    def test_get_specific_application_failure(self):

        #exact same test, but an error in the justification

        self.authorize_as_user(self.user)

        #using university id as identification
        self.url = "/application/getApplications/?uni=" + str(self.uni_id) + "&subject=&approval="
        response = self.get(self.url)

        #asserting that justification is not equal
        self.assertNotEqual(response.data[0]["justification"],"Wrong justification",msg=response.data)