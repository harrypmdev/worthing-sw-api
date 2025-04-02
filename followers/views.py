"""Views file that defines two API views for the Comment app.
FollowerList -- A list view for the 'followers/' endpoint.
FollowerDetail -- A detail view for the 'followers/<int:pk>/' endpoint.
"""

from rest_framework import generics, permissions
from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """Defines the API view for 'followers/' endpoint.
    Utilises a generic Django view to allow for GET and POST requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for authenticated users.
    queryset -- defines the relevant queryset for the list view as all Followers ordered by date
                of creation.

    Methods:
    perform_create -- defines a custom create method so any created Follower is associated with the
                      current User.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """Defines the API view for 'followers/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET and DELETE requests.

    Fields:
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and delete requests for the Follower's owner only.
    serializer_class -- attaches the relevant serializer.
    queryset -- defines the relevant queryset as all Followers.
    """
    permission_classes = [IsUserOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
