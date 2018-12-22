"""
Provides access to settings.
Returns defaults if not set.
"""
from datetime import timedelta

from django.conf import settings


class CustomSettings(object):

    """Provides settings as defaults for working with tokens."""

    @property
    def EXPIRING_TOKEN_DURATION(self):
        """
        Return the allowed lifespan of a token as a TimeDelta object.
        Defaults to 1 day.
        """
        try:
            val = settings.EXPIRING_TOKEN_DURATION
        except AttributeError:
            val = timedelta(days=1)

        return val


custom_settings = CustomSettings()
