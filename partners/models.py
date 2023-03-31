from django.contrib.gis.db import models
import uuid
# Create your models here.


BANK_PARTNER_TYPE = (
    ('Entertainment', 'Entertainment'),
    ('BankRelated', 'BankRelated'),
    ('Shops', 'Shops'),
    ('Services', 'Services'),
    ('Food', 'Food'),
    ('Generic', 'Generic'),

)


class Partner(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=200)
    partner_type = models.CharField(
        choices=BANK_PARTNER_TYPE, default=BANK_PARTNER_TYPE[-1][0], max_length=100)
    rating = models.IntegerField(blank=True, null=True)
    desc = models.TextField(max_length=400)

    # Geo Location Based
    address = models.TextField(max_length=300, blank=True, null=True)
    location = models.PointField(blank=True, null=True)

    # Timings
    # Use a json field to capture the data.
    timings = models.JSONField(blank=True, null=True, default={
                               "everyday": True, "24/7": True})

    # Mode's of communication
    phone = models.CharField(max_length=10, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    # carousel_of_images

    # Product Catalogue
    catalogue = models.JSONField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name+" "+self.partner_type


# Offer Model
class Offer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    statement = models.CharField(max_length=200)
    desc = models.TextField(max_length=400)

    # Time Related
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    # Financial Aspect
    discount = models.IntegerField(blank=True, null=True)
    is_cashback = models.BooleanField(default=False)
    cashback_amt = models.BigIntegerField(blank=True, null=True)

    # To Check Validity
    meta_data = models.JSONField(default=dict({
        "partners": [],
        "bank_types": []
    }))

    def checkUser_valid(self, user_id):
        '''
        Check if the BankDetails's type is in the list given in the meta_data partners or not
        '''
        # Retrieve the user's bank details
        try:
            user_bank_details = Partner.objects.get(account=user_id)
        except Partner.DoesNotExist:
            return False

        # Check if the user's bank type is in the list of valid bank types for the coupon
        if user_bank_details.partner_type in self.meta_data.get('bank_types', []):
            return True
        else:
            return False
