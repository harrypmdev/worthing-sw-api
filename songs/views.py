from rest_framework import generics, permissions
from worthing_sw_api.permissions import IsUserOrReadOnly

from .models import Song
from .serializers import SongSerializer


class SongList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Song.objects.order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Song.objects.order_by('-created_at')
