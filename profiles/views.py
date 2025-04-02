"""Views file that defines two API views for the Profile app.
ProfileList -- A list view for the 'profiles/' endpoint.
ProfileDetail -- A detail view for the 'profiles/<int:pk>/' endpoint.
"""

from django.db.models import Count
from rest_framework import generics

from worthing_sw_api.permissions import IsUserOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """Defines the API view for 'profiles/' endpoint.
    Utilises a generic Django view to allow for GET requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    queryset -- defines the relevant queryset for the list view as all Profiles ordered by date
                of creation. Annotates aggregated values of posts_count, songs_count,
                followers_count and following_count.
    """

    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count("user__post", distinct=True),
        songs_count=Count("user__song", distinct=True),
        followers_count=Count("user__followed", distinct=True),
        following_count=Count("user__following", distinct=True),
    ).order_by("-created_at")


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Defines the API view for 'profiles/<int:pk>/' endpoint.
    Utilises a generic Django view to allow for GET and PUT requests.

    Fields:
    serializer_class -- attaches the relevant serializer.
    permission_classes -- defines the permissions for access to the view. Allows read-only
                          requests for all users and write requests for the Profile's owner only.
    queryset -- defines the relevant queryset for as all Profiles, annotated with aggregated values
                of posts_count, songs_count, followers_count and following_count.
    """

    serializer_class = ProfileSerializer
    permission_classes = [IsUserOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count("user__post", distinct=True),
        songs_count=Count("user__song", distinct=True),
        followers_count=Count("user__followed", distinct=True),
        following_count=Count("user__following", distinct=True),
    )
