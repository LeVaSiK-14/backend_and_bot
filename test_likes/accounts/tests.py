import json

from django.contrib.auth import get_user_model
from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {'username': "Levasik", 'password': "qwertyui12345"}
        response = self.client.post('/api/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


