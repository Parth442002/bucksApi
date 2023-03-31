from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
# Local Imports
from .models import Partner
from .serializers import BankPartnerDetailsSerializer


class AllBankDetailsListView(generics.ListCreateAPIView):
    queryset = Partner.objects.all()
    serializer_class = BankPartnerDetailsSerializer
    permission_classes = [permissions.AllowAny]


class UserNearbyPartnersView(APIView):

    def post(self, request, format=None):
        # Get the longitude, latitude, and radius from the request body
        longitude = request.data.get('longitude', None)
        latitude = request.data.get('latitude', None)
        radius = request.data.get('radius', None)

        # Validate that all parameters are provided
        if not all([longitude, latitude, radius]):
            return Response({'error': 'Longitude, latitude, and radius are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert the longitude, latitude, and radius to floats
        try:
            longitude = float(longitude)
            latitude = float(latitude)
            radius = float(radius)
        except ValueError:
            return Response({'error': 'Longitude, latitude, and radius must be valid floats.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a Point object for the user's location
        user_location = Point(longitude, latitude, srid=4326)

        # Filter the Places within the radius of the user's location
        queryset = Partner.objects.annotate(distance=Distance(
            'location', user_location)).filter(distance__lte=radius).order_by("distance")

        # Serialize the queryset using the PartnerSerializer
        serializer = BankPartnerDetailsSerializer(queryset, many=True)

        # Return the serialized data as JSON
        return Response(serializer.data)
