from rest_framework import serializers, permissions
from .models import BankDetail, BankCards


class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = ("__all__")


class CardDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCards
        fields = ("__all__")
