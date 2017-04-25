from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test import Client
from application.models import Application
from subjects.models import Subject
from universities.models import University

# Create your tests here.
setup_test_environment()
client = Client()

class ApplicationViewTests(TestCase):

    def setUp(self):

        u1 = University.objects.create(title="ETH", country="Switzerland", city="Zurich", description = "Cool class")

        s1 = Subject.objects.create(university=u1, title="Objectoriented Programming", courseCode = "TDT4240",
                                    ntnuCredits = 12, description = "Great class" )
        s2 = Subject.objects.create(university=u1, title="C++", courseCode="ETH5555",
                                    ntnuCredits=12, description="Great class")
        Application.objects.create(user = "Axel",
                                   ntnu_subject = s1,
                                   replacing_subject= s2,
                                   justification="Great class",
                                   application_status=STATUS_PROCESSING);


