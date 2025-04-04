"""Views file that defines two API views for the Post app.
PostList -- A list view for the 'posts/' endpoint.
PostDetail -- A detail view for the 'posts/<int:pk>/' endpoint.
"""

from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """Defines the API view for 'posts/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for authenticated users.
    queryset -- defines the relevant queryset for the list view as all Posts ordered by date
                of creation.
    filter_backends -- enables field filtering, ordering and search filtering.
    search_fields -- enables searching by associated user's username and post title.
    filterset_fields -- enables filtering by user id, user's profile id, following, following by
                        by profile id and net votes.
    ordering_fields -- enables ordering by net votes.

    Methods:
    perform_create -- defines a custom create method so any created post is associated with the
                      current User.
    """

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["user__username", "title"]
    filterset_fields = [
        "user",
        "user__profile",
        "user__followed__user",
        "user__followed__user__profile",
        "net_votes",
    ]
    ordering_fields = ["net_votes", "created_at"]

    def perform_create(self, serializer):
        """Custom create method to attach the current User to the new song instance."""
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the API view for 'posts/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET, PUT and DELETE requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the Post's owner only.
    queryset -- defines the relevant queryset as all Posts.
    """

    serializer_class = PostSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Post.objects
