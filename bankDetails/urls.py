from django.urls import path

# Local Imports
from . import views

urlpatterns = [
    path("", views.RetriveBankDetails.as_view()),
    path("create/", views.CreateBankDetails.as_view()),
    path("cards/buy/", views.BuyCardView.as_view()),
]
