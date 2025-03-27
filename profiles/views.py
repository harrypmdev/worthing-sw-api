from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('user__post', distinct=True),
        songs_count=Count('user__song', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    ordering_fields = [
        'posts_count',
        'songs_count',
        'followers_count',
        'following_count',
        'user__following__created_at',
        'user__folowed__created_at'
    ]
    filterset_fields = [
        'user__following__followed__profile',
        'user__followed__user__profile'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('user__post', distinct=True),
        songs_count=Count('user__song', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True)
    ).order_by('-created_at')
