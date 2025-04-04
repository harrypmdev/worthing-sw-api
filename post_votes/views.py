"""Views file that defines two API views for the post_votes app.
PostVoteList -- A list view for the 'post_votes/' endpoint.
PostVoteDetail -- A detail view for the 'post_votes/<int:pk>/' endpoint.
"""

from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import PostVote
from .serializers import PostVoteSerializer


class PostVoteList(generics.ListCreateAPIView):
    """Defines the API view for 'post_votes/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                            requests for all users and write requests for authenticated users.
    queryset -- defines the relevant queryset for the list view as all PostVotes ordered by date
                of creation.
    filter_backends -- enables field filtering.
    filterset_fields -- enables filtering by user.

    Methods:
    perform_create -- defines a custom create method so any created PostVote is associated with the
                      current User.
    """

    serializer_class = PostVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostVote.objects.order_by("-created_at")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user"]

    def perform_create(self, serializer):
        """Custom create method to attach the current User to the new song instance."""
        serializer.save(user=self.request.user)


class PostVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the API view for 'post_votes/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET, PUT and DELETE requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the PostVote's owner only.
    queryset -- defines the relevant queryset as all PostVotes.
    """

    serializer_class = PostVoteSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = PostVote.objects
