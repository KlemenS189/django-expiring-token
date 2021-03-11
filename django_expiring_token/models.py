import binascii
import os

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from django_expiring_token.settings import custom_settings


class ExpiringToken(models.Model):
    class Meta:
        db_table = 'expiring_authtoken'
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    key = models.CharField(_("Key"), max_length=50, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    expires = models.DateTimeField(_("Expires in"), db_index=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()

        self.expires = timezone.now() + custom_settings.EXPIRING_TOKEN_DURATION
        return super(ExpiringToken, self).save(*args, **kwargs)

    def generate_key(self) -> str:
        return binascii.hexlify(os.urandom(25)).decode()

    def __str__(self):
        return self.key
