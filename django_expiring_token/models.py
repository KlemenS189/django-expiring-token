import secrets

from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.db import models
from django.utils.translation import gettext as _

from django_expiring_token.settings import custom_settings


class ExpiringToken(Token):
    key = models.CharField(_("Key"), max_length=45, primary_key=True)
    expires = models.DateTimeField(_("Expires in"), )

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()

        self.expires = timezone.now() + custom_settings.EXPIRING_TOKEN_DURATION
        return super(ExpiringToken, self).save(*args, **kwargs)

    def generate_key(self):
        return secrets.token_urlsafe(32)