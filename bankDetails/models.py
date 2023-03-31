from django.contrib.gis.db import models
from authentication.models import Account
import uuid
# Create your models here.


BANK_TYPE = (
    ('Silver', 'Silver'),
    ('Gold', 'Gold'),
    ('Platinum', 'Platinum'),
    ('Black', 'Black'),
)


class BankDetail(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    number = models.BigIntegerField(blank=True, null=True)
    ifsc = models.CharField(max_length=11, blank=True, null=True)
    details = models.JSONField(blank=True, null=True)
    bank_type = models.CharField(
        choices=BANK_TYPE,
        default=BANK_TYPE[1][0],
        max_length=100,
    )
    reward_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.account.primary_identifier + "- Bank Details"


class BankCards(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    holder = models.ForeignKey(BankDetail, on_delete=models.CASCADE)
    # TimeData
    valid_from = models.DateField(auto_now_add=True)
    valid_till = models.DateField(blank=True, null=True)

    card_type = models.CharField(default="basic", max_length=100)
    card_perks = models.JSONField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.card_type+" card of "+self.holder.account.primary_identifier
