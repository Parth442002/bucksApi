from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView

# Local Imports
from . import views

urlpatterns = [
    path("login/", TokenObtainPairView.as_view()),
    path("logout/", views.LogoutView.as_view()),
    path("details/", views.AccountDetailsView.as_view()),
    path("verifyToken/", TokenVerifyView.as_view()),
]
