"""URL conf for testing Expiring Tokens."""
from django.urls import path

from django_expiring_token.views import LoginView

urlpatterns = [
    path('obtain-token/', LoginView.as_view(), name='obtain-token'),
]