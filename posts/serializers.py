from rest_framework import serializers

from .models import Post
from post_votes.models import PostVote


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    user_image = serializers.ReadOnlyField(source='user.profile.image.url')
    is_user = serializers.SerializerMethodField()
    user_upvoted = serializers.SerializerMethodField()
    user_downvoted = serializers.SerializerMethodField()
    user_vote_id = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_user_upvoted(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return PostVote.objects.filter(post=obj, user=user, downvote=False).exists()
        return False

    def get_user_downvoted(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return PostVote.objects.filter(post=obj, user=user, downvote=True).exists()
        return False

    def get_user_vote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            vote = PostVote.objects.filter(post=obj, user=user).first()
            return vote.id if vote else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'user_image', 'profile_id',
            'is_user', 'title', 'updated_at',
            'created_at', 'content', 'song', 'net_votes',
            'user_upvoted', 'user_downvoted', 'user_vote_id'
        ]
