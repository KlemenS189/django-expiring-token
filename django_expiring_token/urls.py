from django.urls import path

from django_expiring_token.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]
