import json

from django.db.models.signals import post_save
from django.utils.crypto import get_random_string
from rest_framework.test import APITestCase
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def random_string(length):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    return get_random_string(length, alpha)


def get_random_number(length):
    number = '0123456789'
    return get_random_string(length, number)


def get_random_email():
    return '{}@{}.no'.format(random_string(5), random_string(5))


def create_random_user_data(email=None):
    if not email:
        email = get_random_email()

    return {
        'email': email,
        'first_name': random_string(10),
        'last_name': random_string(10),
        'date_of_birth': '1995-04-04',
        'phone_mobile': get_random_number(8),
        'phone_work': get_random_number(8),
    }


class ExtendedAPITestCase(APITestCase):

    def get(self, url):
        response = self.client.get(url)
        return response

    def post(self, url, data):
        data = json.dumps(data)
        response = self.client.post(url, data, content_type='application/json')
        return response

    def put(self, url, data):
        data = json.dumps(data)
        response = self.client.put(url, data, content_type='application/json')
        return response

    def delete(self, url):
        response = self.client.delete(url)
        return response

    def authorize_as_user(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
