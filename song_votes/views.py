from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import SongVote
from .serializers import SongVoteSerializer


class SongVoteList(generics.ListCreateAPIView):
    serializer_class = SongVoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SongVote.objects.order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SongVoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongVoteSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = SongVote.objects.order_by('-created_at')
