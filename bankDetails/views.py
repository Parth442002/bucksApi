import json
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status, permissions

# Local Imports.
from .functions import getIfsc
from .models import BankDetail, BankCards
from .serializers import BankDetailSerializer, CardDetailsSerializer


def get_object_or_404(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        raise Http404()


# Retrive Bank Details of the Current User
class RetriveBankDetails(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        bank = get_object_or_404(BankDetail, account=request.user.id)
        cards = BankCards.objects.filter(holder__id=bank.id)
        cardSerializer = CardDetailsSerializer(cards, many=True)
        serializer = BankDetailSerializer(bank)
        if serializer:
            res = serializer.data
            res["cards"] = cardSerializer.data
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateBankDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request,):
        details = getIfsc(ifsc=request.data.get("ifsc"))
        dataObj = {
            "account": request.data.get("account"),
            "number": request.data.get("number"),
            "ifsc": request.data.get("ifsc"),
            "details": details,
        }
        serializer = BankDetailSerializer(data=dataObj)

        if serializer.is_valid():
            # Write a specific mail to each and every participant
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BuyCardView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = CardDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # Specific Functions that should take place
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCardView(APIView):
    permission_classes = (permissions.AllowAny,)

    def patch(self, request, card_id):
        card = get_object_or_404(BankCards, id=card_id)
        serializer = CardDetailsSerializer(
            card, data=request.data, partial=True)
        if serializer.is_valid():
            # The data which is passed is accurate
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class receiveRewardsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, bank_id, amount):
        bank = get_object_or_404(BankDetail, id=bank_id)
        if amount > 0:
            total = bank.reward_points+amount
            serializer = BankDetailSerializer(
                bank, data={"reward_points": total}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SpendRewardsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, bank_id, amount):
        bank = get_object_or_404(BankDetail, id=bank_id)
        if amount <= bank.reward_points:
            total = bank.reward_points-amount
            serializer = BankDetailSerializer(
                bank, data={"reward_points": total}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
