from rest_framework import generics, permissions
from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsUserOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
