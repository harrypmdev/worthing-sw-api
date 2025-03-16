from rest_framework import serializers

from .models import Song
from votes.models import Vote


class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    audio_url = serializers.ReadOnlyField()
    net_votes = serializers.SerializerMethodField()

    def get_net_votes(self, obj):
        votes = Vote.objects.filter(
            content_type__model='song',
            object_id=obj.id
        )
        upvotes = votes.filter(downvote=False).count()
        downvotes = votes.filter(downvote=True).count()
        return upvotes - downvotes

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Song
        fields = [
            'id', 'user', 'is_user', 'title', 'updated_at', 'created_at',
            'artist_name', 'posts', 'audio_url', 'net_votes'
        ]
