import binascii
import os

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token

from django_expiring_token.settings import custom_settings


class ExpiringToken(Token):
    key = models.CharField(_("Key"), max_length=50, primary_key=True)
    expires = models.DateTimeField(_("Expires in"), )

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()

        self.expires = timezone.now() + custom_settings.EXPIRING_TOKEN_DURATION
        return super(ExpiringToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(25)).decode()
