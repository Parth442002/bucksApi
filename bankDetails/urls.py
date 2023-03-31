from django.urls import path

# Local Imports
from . import views

urlpatterns = [
    path("", views.RetriveBankDetails.as_view()),
    path("create/", views.CreateBankDetails.as_view()),
    path("cards/buy/", views.BuyCardView.as_view()),
    path("cards/update/<uuid:card_id>/", views.UpdateCardView.as_view()),
    path("rewards/<int:bank_id>/amount=<int:amount>",
         views.receiveRewardsView.as_view()),
    path("rewards/spend/<int:bank_id>/amount=<int:amount>",
         views.SpendRewardsView.as_view()),
]
