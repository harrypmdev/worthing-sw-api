"""Views file that defines three API views for the venues app.
VenueList -- A list view for the 'venues/' endpoint.
UserVenueList -- A list view for the 'user_venues/' endpoint.
UserVenueDetail -- A detail view for the 'user_venues/<int:pk>/' endpoint.
"""

from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Venue, UserVenue
from .serializers import VenueSerializer, UserVenueSerializer


class VenueList(generics.ListAPIView):
    """Defines the API view for 'venues/' endpoint.
    Utilises a generic Django view to allow for GET requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    queryset -- defines the relevant queryset for the list view as all venues.
    """
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer


class UserVenueList(generics.ListCreateAPIView):
    """Defines the API view for 'user_venues/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    queryset -- defines the relevant queryset for the list view as all UserVenues.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for authenticated users.
    serializer_class -- attaches the relevant serializer.
    filter_backends -- enables field filtering.
    filterset_fields -- enables filtering by user and venue fields.
    """
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
    """Defines the API view for 'user_venues/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET and DELETE requests.

    Fields:
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the UserVenue's owner only.
    serializer_class -- attaches the relevant serializer.
    queryset -- defines the relevant queryset as all UserVenues.
    """
    permission_classes = [IsUserOrReadOnly]
    serializer_class = UserVenueSerializer
    queryset = UserVenue.objects.all()
