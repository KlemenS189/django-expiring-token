import os
import sys

from setuptools import setup

import django_expiring_token

version = django_expiring_token.__version__

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if sys.argv[-1] == 'publish':
    if os.system("pip list | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name='django-expiring-token',
    version=version,
    packages=['django_expiring_token', 'django_expiring_token.migrations'],
    install_requires=[
        'djangorestframework>=3.4.0'
    ],
    test_suite='runtests.run',
    tests_require=[
        'Django>=2.0.8'
    ],
    include_package_data=True,
    license='MIT License',  # example license
    description='Expiring token with expiration time update for Django Rest Framework',
    long_description=README,
    author='Klemen Štrajhar',
    url='https://github.com/KlemenS189/django_expiring_token',
    author_email='klemen.strajhar@gmail.si',
    classifiers=[
        'Development Status :: 1 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)