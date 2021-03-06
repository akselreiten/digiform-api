from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from digiform_api.utils.test_mixins import ExtendedAPITestCase
from digiform_api.utils.test_factory import create_user, create_university
from django.urls import reverse
from universities.models import University
from rest_framework import status


# Create your tests here.

class CreateUniversityReviewTest(ExtendedAPITestCase):

    def setUp(self):
        #need a user and a university
        self.user = create_user()
        self.university = create_university()

    def test_create_university_review(self):
        #attributes
        data = {
            "user":self.user.id,
            "lectures_rating":"5",
            "assignments_rating":"4",
            "difficulty_rating":"3",
            "social_rating":"2",
            "course_availability_rating":"2",
            "price_rating":"3",
            "university":self.university.id,
            "description":"Great school. Good times."
        }

        self.url = reverse("university-review-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED,msg=response.data)

    def test_unauth_create_university_review(self):
        data = {
            "user":self.user.id,
            "lectures_rating":"5",
            "assignments_rating":"4",
            "difficulty_rating":"3",
            "social_rating":"2",
            "course_availability_rating":"2",
            "price_rating":"3",
            "university":self.university.id,
            "description":"Great school. Good times."
        }

        self.url = reverse("university-review-list-create")
        #not authorizing
        response = self.post(self.url,data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

class GetUniversityReviewTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()

    def test_get_university_review(self):
        self.authorize_as_user(self.user)
        self.url = "/university_reviews/?uni=" #filtering in all reviews
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK,msg=response.data)

    def test_unauth_get_university_review(self):
        #not authorizing
        self.url = "/university_reviews/?uni=/"
        response = self.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED,msg=response.data)

class GetSpecificUniversityReviewTest(ExtendedAPITestCase):

    def setUp(self):
        self.user = create_user()
        self.university = University.objects.create(
            title = "Test university",
            city = "Trondheim",
            country = "Norway",
            description = "Fantastic."
        )

        data = {
            "user":self.user.id,
            "lectures_rating":"5",
            "assignments_rating":"4",
            "difficulty_rating":"3",
            "social_rating":"2",
            "course_availability_rating":"2",
            "price_rating":"3",
            "university":self.university.id,
            "description":"Great school. Good times."
        }

        self.url = reverse("university-review-list-create")
        self.authorize_as_user(self.user)
        response = self.post(self.url,data) #adding review in test database

    def test_get_specific_university_review(self):

        self.authorize_as_user(self.user)
        self.url = "/university_reviews/?uni=1" #filtering in the first (and only) entry in test database
        response = self.get(self.url)

        #check if correct description
        self.assertEqual(response.data[0]["description"],"Great school. Good times.",msg=response.data)