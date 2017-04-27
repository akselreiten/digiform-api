import json

from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

#test methods used throughout the test functions

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def random_string(length): #used for name generation
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return get_random_string(length, alpha)

def get_random_email(): #email generation
    return '{}@{}.no'.format(random_string(5), random_string(5))


class ExtendedAPITestCase(APITestCase):

    def get(self, url):  #get from database
        response = self.client.get(url)
        return response

    def post(self, url, data): #insert into database
        data = json.dumps(data)
        response = self.client.post(url, data, content_type='application/json')
        return response

    def authorize_as_user(self, user): #authorize user
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
