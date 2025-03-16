from rest_framework import serializers

from .models import Post
from songs.models import Song
from votes.models import Vote


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    songs = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Song.objects.all(),
        required=False
    )
    net_votes = serializers.SerializerMethodField()

    def get_net_votes(self, obj):
        votes = Vote.objects.filter(
            content_type__model='post',
            object_id=obj.id
        )
        upvotes = votes.filter(downvote=False).count()
        downvotes = votes.filter(downvote=True).count()
        return upvotes - downvotes

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def validate_songs(self, value):
        if len(value) > 3:
            raise serializers.ValidationError('A post cannot have more than 3 songs attached.')
        return value

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'is_user', 'title', 'updated_at',
            'created_at', 'content', 'songs', 'net_votes'
        ]
