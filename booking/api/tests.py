from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory
from rest_framework import status
from knox.models import AuthToken
from django.contrib.auth.models import User

class BookTicketsTest(APITestCase):
    def setUp(self):
        self.username = 'john.doe'
        self.email = 'john.doe@example.com'
        self.password = 'hunter2'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = AuthToken.objects.create(self.user)[1]

    def test_get_ticket_details(self):
        """
            Ensure we can get ticket details
        """
        url = '/book/api/v1/booking/'
        response = self.client.get(url, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)