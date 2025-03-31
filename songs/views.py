from django.core.exceptions import ValidationError
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Song
from .serializers import SongSerializer


class SongList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Song.objects.order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'user__username',
        'title'
    ]
    filterset_fields = [
        'user',
        'user__profile',
        'user__followed__user',
        'net_votes'
    ]
    ordering_fields = [
        'net_votes'
    ]

    def perform_create(self, serializer):
        user = self.request.user
        song_count = Song.objects.filter(user=user).count()
        if song_count >= 3:
            raise ValidationError('You cannot add more than 3 songs')
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        limit = self.request.query_params.get('limit')
        if limit is not None:
            queryset = queryset[:int(limit)]
        return queryset


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Song.objects.order_by('-created_at')
