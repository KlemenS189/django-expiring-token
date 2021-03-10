"""URL conf for testing Expiring Tokens."""
from django.urls import include
from django.urls import path

from django_expiring_token.views import LoginView

urlpatterns = [
    path('obtain-token/', LoginView.as_view(), name='obtain-token'),
    path('custom-url/', include('django_expiring_token.urls'))
]