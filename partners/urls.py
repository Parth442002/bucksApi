from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllBankDetailsListView.as_view()),
    path("nearby/", views.UserNearbyPartnersView.as_view()),
]
