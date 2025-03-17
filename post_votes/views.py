from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import PostVote
from .serializers import PostVoteSerializer


class PostVoteList(generics.ListCreateAPIView):
    serializer_class = PostVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = PostVote.objects.order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostVoteSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = PostVote.objects.order_by('-created_at')
