"""Views file that defines two API views for the Song app.
SongList -- A list view for the 'songs/' endpoint.
SongDetail -- A detail view for the 'songs/<int:pk>/' endpoint.
"""

from django.core.exceptions import ValidationError
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Song
from .serializers import SongSerializer


class SongList(generics.ListCreateAPIView):
    """Defines the API view for 'songs/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for authenticated users.
    queryset -- defines the relevant queryset for the list view as all Songs ordered by date
                of creation.
    filter_backends -- enables filed filtering and ordering.
    filterset_fields -- enables filtering by user id, user's profile id, following and net votes.
    ordering_fields -- enables ordering by net votes.

    Methods:
    perform_create -- defines a custom create method which disallows the creation of more than
                      3 songs per User.
    get_queryset -- defines a custom method for retrieving the queryset which limits the queryset
                    to a cap if a limit is given.
    """

    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Song.objects.order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = ["user", "user__profile", "user__followed__user", "net_votes"]
    ordering_fields = ["net_votes"]

    def perform_create(self, serializer):
        """Custom create method to ensure users cannot have more than 3 songs."""
        user = self.request.user
        song_count = Song.objects.filter(user=user).count()
        if song_count >= 3:
            raise ValidationError("You cannot add more than 3 songs")
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Custom queryset method which limits the retrieved songs if a limit is provided."""
        queryset = super().get_queryset()
        limit = self.request.query_params.get("limit")
        if limit is not None:
            queryset = queryset[: int(limit)]
        return queryset


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the API view for 'songs/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET, PUT and DELETE requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the Song's owner only.
    queryset -- defines the relevant queryset as all Songs.
    """

    serializer_class = SongSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Song.objects
