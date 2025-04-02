"""Views file that defines two API views for the Comment app.
CommentList -- A list view for the 'comments/' endpoint.
CommentDetail -- A detail view for the 'comments/<int:pk>/' endpoint.
"""

from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """Defines the API view for 'comments/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for authenticated users.
    queryset -- defines the relevant queryset for the list view as all Posts ordered by date
                of creation.
    filter_backends -- enables field filtering.
    filterset_fields -- enables filtering by user and post.

    Methods:
    perform_create -- defines a custom create method so any created comment is associated with the
                      current User.
    """

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.order_by("-created_at")
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "post"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Defines the API view for 'comments/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET, PUT and DELETE requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the Comment's owner only.
    queryset -- defines the relevant queryset as all Comments.
    """

    serializer_class = CommentDetailSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Comment.objects.all()
