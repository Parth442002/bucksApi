from django.contrib.auth import get_user_model
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken


# Local Imports
from .serializers import CustomTokenObtainPairSerializer, AccountDetailsSerializer

# Settings the User Model
user_model = get_user_model()


class AccountDetailsView(APIView):
    '''
    Display the Account Details
    '''
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        serializer = AccountDetailsSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            access_token = request.data["access"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
