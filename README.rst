=====================
Django Expiring Token
=====================

Django Expiring Token adds token expiration on token authentication and extends the
expiration time on each authenticated request.

Django Expiring Token provides a very lightweight extension to DRF's existing token authentication.
It implements the following functionalities:

1. Tokens expire after the set time.
2. On each authenticated request, the expiration time is updated by the set time.

Quick start
-----------
1. Do NOT add "restframework.authtoken" to you INSTALLED_APPS.

2. Add "django_expiring_token" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_expiring_token',
    ]

3. Include the polls URLconf in your project urls.py like this::

    path('custom-url/', include('django_expiring_token.urls')),

4. Add the expiration time in `settings.py`::

    EXPIRING_TOKEN_DURATION=timedelta(hours=1)
    # Any timedelta setting can be used!

4. Run `python manage.py migrate` to create the ExpiringToken model.

5. Start the development server.
