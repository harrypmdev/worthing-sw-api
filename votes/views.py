from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Vote
from .serializers import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Vote.objects.order_by('-created_at')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['content_type', 'object_id']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VoteDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Vote.objects.order_by('-created_at')
