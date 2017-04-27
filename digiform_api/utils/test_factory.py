from django.contrib.auth.models import User
from universities.models import University
from subjects.models import Subject
from test_mixins import random_string, get_random_email
import uuid

def create_user():
    id = str(uuid.uuid4())
    return User.objects.create(username=id,
                               email=id + '@test.no',
                               password='secret',
                               first_name=random_string(5),
                               last_name='bruker',
                               )

def create_other_user():
    id = str(uuid.uuid4())
    return User.objects.create(username=id,
                               email=id + '@test.no',
                               password='secret',
                               first_name=random_string(5),
                               last_name=random_string(5)+'sen',
                               )

def create_ntnu():
    id = str(uuid.uuid4())
    return University.objects.create(title="NTNU",
                                     city="Trondheim",
                                     country="Norway",
                                     description="The best. Terrific university really")

def create_university():
    id = str(uuid.uuid4())
    return University.objects.create(title="Test University",
                                     city="Test City",
                                     country="Testland",
                                     description="Cool university")

def create_ntnu_subject():
    id = str(uuid.uuid4())
    return Subject.objects.create(university=create_ntnu(),
                                  title="Objectoriented Programming",
                                  courseCode = "TDT4240",
                                  ntnuCredits = 12,
                                  description = "Great class" )

def create_foreign_subject():
    id = str(uuid.uuid4())
    return Subject.objects.create(university=create_university(),
                                  title="C++",
                                  courseCode="ETH5555",
                                  ntnuCredits=12,
                                  description="Great class")

def get_basic_user_data():
    return {
        'username': random_string(10),
        'email': get_random_email(),
        'password': random_string(10)
    }