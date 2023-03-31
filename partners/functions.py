from django.utils import timezone
from datetime import date
from .models import Offer, Partner
from bankDetails.models import BankDetail


def get_valid_offers(bank_detail_id, partner_id):
    valid_offers = []
    today = date.today()
    try:
        partner = Partner.objects.get(id=partner_id)
        bank = BankDetail.objects.get(id=bank_detail_id)
        for offer in Offer.objects.filter(start__lte=today, end__gte=today):
            if bank.bank_type in offer.meta_data.get('bank_types', []) and partner.id in offer.meta_data.get('partners', []):
                valid_offers.append(offer)
    except Partner.DoesNotExist:
        pass
    return valid_offers
