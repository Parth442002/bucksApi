from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Account


# Login Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["primary_identifier"] = user.primary_identifier
        return token


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        geo_field = 'location'
        fields = ['id', 'primary_identifier',
                  'email', 'phone', 'fullname', 'location']
