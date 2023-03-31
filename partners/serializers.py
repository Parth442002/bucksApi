from rest_framework import serializers

from .models import Partner


class BankPartnerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        geo_field = 'location'
        fields = ['id', 'name', 'desc', 'location',
                  'address', 'timings', 'catalogue', 'phone', 'website', 'email', 'rating']
