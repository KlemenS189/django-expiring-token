# Django Expiring Token

[![Requirements Status](https://requires.io/github/KlemenS189/django-expiring-token/requirements.svg?branch=master)](https://requires.io/github/KlemenS189/django-expiring-token/requirements/?branch=master)   [![Build Status](https://travis-ci.org/KlemenS189/django-expiring-token.svg?branch=master)](https://travis-ci.org/KlemenS189/django-expiring-token) [![Coverage Status](https://coveralls.io/repos/github/KlemenS189/django-expiring-token/badge.svg?branch=master)](https://coveralls.io/github/KlemenS189/django-expiring-token?branch=master)
[![PyPI pyversions](https://img.shields.io/badge/python-3.6%20|%203.7%20|%203.8%20|%203.9-blue.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI pyversions](https://img.shields.io/badge/django-2.2%2B-blue.svg)](https://pypi.python.org/pypi/ansicolortags/)




## Introduction
Django Expiring Token provides a very lightweight extension to DRF's existing token authentication.
It implements the following functionalities:

1. Tokens expire after the set time.
2. On each authenticated request, the expiration time is updated by the set time in ```settings.py.```

## Quick setup

1. Do NOT add ```restframework.authtoken``` to your ```INSTALLED_APPS```.
2. Add ```django_expiring_token``` to your ```INSTALLED_APPS``` setting like this:
    ```
    INSTALLED_APPS = [
        ...
        'rest_framework',
        'django_expiring_token',
    ]
    ```

3. Include the URLconf in your project urls.py like this:
    ```
    path('custom-url/', include('django_expiring_token.urls')),
    ```
4. Add the expiration time in `settings.py`:
    ```
    EXPIRING_TOKEN_DURATION = timedelta(hours=1)
    # Any timedelta setting can be used! If not set, the default value is 1 day
    ```
5. Add the default authentication class in ```REST_FRAMEWORK``` settings in ```settings.py```
    ```
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            ...
            'django_expiring_token.authentication.ExpiringTokenAuthentication',
            ...
        ),
    }
    ```
5. Run `python manage.py migrate` to create package migrations

6. Start the development server and you are good to go.

## Tests
This build is tested against Python versions 3.6, 3.7, 3.8, 3.9 with Django versions 2.2+
To run tests
1. Install ```coverage```
    ```
    pip install coverage
    ```
2. Run tests
    ```
    coverage run runtest.py
    ```





