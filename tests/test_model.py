from datetime import timedelta
from time import sleep

from django.contrib.auth.models import User
from django.test import TestCase

from django_expiring_token.authentication import ExpiringTokenAuthentication, is_token_expired
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

        self.test_instance = ExpiringTokenAuthentication()

    def test_non_expired(self):
        self.assertFalse(is_token_expired(self.token))

    def test_expired_token(self):
        # let the token expire
        sleep(0.1)
        self.assertTrue(is_token_expired(self.token))
