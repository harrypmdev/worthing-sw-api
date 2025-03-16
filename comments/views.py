from rest_framework import generics, permissions

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Comment.objects.order_by('-created_at')
