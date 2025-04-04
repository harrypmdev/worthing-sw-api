"""Views file that defines two API views for the song_votes app.
SongVoteList -- A list view for the 'song_votes/' endpoint.
SongVoteDetail -- A detail view for the 'song_votes/<int:pk>/' endpoint.
"""

from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import SongVote
from .serializers import SongVoteSerializer


class SongVoteList(generics.ListCreateAPIView):
    """Defines the API view for 'songs_votes/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                            requests for all users and write requests for authenticated users.
    queryset -- defines the relevant queryset for the list view as all SongVotes ordered by date
                of creation.
    filter_backends -- enables field filtering.
    filterset_fields -- enables filtering by user.

    Methods:
    perform_create -- defines a custom create method so any created SongVote is associated with the
                      current User.
    """

    serializer_class = SongVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SongVote.objects.order_by("-created_at")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]

    def perform_create(self, serializer):
        """Custom create method to attach the current User to the new song instance."""
        serializer.save(user=self.request.user)


class SongVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the API view for 'song_votes/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET, PUT and DELETE requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the SongVote's owner only.
    queryset -- defines the relevant queryset as all SongVotes.
    """

    serializer_class = SongVoteSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = SongVote.objects
