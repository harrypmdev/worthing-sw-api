from rest_framework import serializers

from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.pk')
    is_user = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    songs_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                user=user, followed=obj.user
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'user_id', 'bio', 'created_at',
            'image', 'is_user', 'following_id',
            'following_count', 'followers_count',
            'posts_count', 'songs_count'
        ]
