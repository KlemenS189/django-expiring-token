from datetime import timedelta
from time import sleep

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from django_expiring_token.models import ExpiringToken


class ExpiringTokenAuthenticationTestCase(TestCase):
    """Test the authentication class directly."""

    def setUp(self):
        """Create a user and associated token."""
        self.username = 'test_username'
        self.email = 'test@g.com'
        self.password = 'test_password'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

        self.key = 'jhfbgkjasnlkfmlkn'
        self.token = ExpiringToken.objects.create(
            user=self.user,
            key=self.key
        )
        self.client = APIClient()

    def test_create_token(self):
        user = User.objects.create_user(
            username="test",
            email="",
            password="abcd1234"
        )
        data = {'username': 'test', 'password': 'abcd1234'}
        resp = self.client.post(reverse('obtain-token'), data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_obtain_token_no_credentials(self):
        resp = self.client.post(reverse('obtain-token'))
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_obtain_token_bad_credentials(self):
        data = {'username': 'test_username', 'password': 'blblb'}
        resp = self.client.post(reverse('obtain-token'), data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resp.data['detail'], 'Invalid Credentials')

    def test_obtain_token_good_credentials(self):
        data = {'username': 'test_username', 'password': 'test_password'}
        resp = self.client.post(reverse('obtain-token'), data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(self.key, resp.data['token'])

    def test_obtain_token_inactive_user(self):
        username = 'test_username_non_active'
        email = 'test@gg.com'
        password = 'test_password'
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_active = False
        user.save()

        data = {'username': 'test_username_non_active', 'password': 'test_password'}
        resp = self.client.post(reverse('obtain-token'), data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resp.data['detail'], 'Invalid Credentials')

    def test_replace_expired_token(self):
        self.token.delete()
        token = ExpiringToken.objects.create(user=self.user)
        key_1 = token.key

        data = {'username': 'test_username', 'password': 'test_password'}

        with self.settings(EXPIRING_TOKEN_DURATION=timedelta(milliseconds=1)):
            sleep(0.005)
            resp = self.client.post(reverse('obtain-token'), data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        token = ExpiringToken.objects.first()
        key_2 = token.key
        self.assertEqual(token.user, self.user)
        self.assertEqual(resp.data['token'], token.key)
        self.assertTrue(key_1 != key_2)

