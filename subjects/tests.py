from django.test import TestCase
from digiform_api.utils.test_mixins import ExtendedAPITestCase
from digiform_api.utils.test_factory import create_user, create_university, create_foreign_subject
from django.urls import reverse
from rest_framework import status

# Create your tests here.

class CreateSubjectTest(ExtendedAPITestCase):
    def setUp(self):
        #need user and university
        self.user = create_user()
        self.university = create_university()


    def test_create_subject(self):
        data = {
            "university":self.university.id,
            "title":"Test Subject",
            "courseCode":"ABC321",
            "ntnuCredits":"10",
            "description":"Great subject"
        }

        self.url = reverse("subject-list-create") #url
        self.authorize_as_user(self.user) #auth
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)

    def test_unauth_create_subject(self):
        data = {
            "university":self.university.id,
            "title":"Test Subject",
            "courseCode":"ABC321",
            "ntnuCredits":"10",
            "description":"Great subject"
        }

        self.url = reverse("subject-list-create")
        #not auth
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED, msg=response.data)


class GetSubjectTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_subject(self):

        self.authorize_as_user(self.user)
        self.url = "/subjects/1/" #subject with id 1, first and only subject in test database
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data) #200 ok

    def test_unauth_get_subject(self):
        self.url = "/subjects/1/"
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

class GetSpecificSubjectTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.university = create_university()

        data = {
            "university":self.university.id,
            "title":"A very specific name for a test subject",
            "courseCode":"ABC321",
            "ntnuCredits":"10",
            "description":"Great subject"
        }

        self.url = reverse("subject-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)

    def test_get_specific_subject(self):

        self.authorize_as_user(self.user)
        self.url = "/subjects/?title=A very specific name for a test subject" #filter on name
        response = self.get(self.url)
        self.assertEqual(response.data["results"][0]["courseCode"],"ABC321",msg=response.data) #check if coursecode is correct

