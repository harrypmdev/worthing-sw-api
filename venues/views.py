from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Venue, UserVenue
from .serializers import VenueSerializer, UserVenueSerializer


class VenueList(generics.ListAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class UserVenueList(generics.ListCreateAPIView):
    queryset = UserVenue.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserVenueSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "user",
        "venue",
    ]


class UserVenueDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsUserOrReadOnly]
    serializer_class = UserVenueSerializer
    queryset = UserVenue.objects.all()
