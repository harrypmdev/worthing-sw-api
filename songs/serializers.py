from rest_framework import serializers

from .models import Song
from song_votes.models import SongVote


class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
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
            return SongVote.objects.filter(song=obj, user=user, downvote=False).exists()
        return False

    def get_user_downvoted(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return SongVote.objects.filter(song=obj, user=user, downvote=True).exists()
        return False

    def get_user_vote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            vote = SongVote.objects.filter(song=obj, user=user).first()
            return vote.id if vote else None
        return None

    def validate_audio_file(self, value):
        if not value:
            raise serializers.ValidationError("An audio file is required.")
        if value.size > 10 * 1024 * 1024:  # 10MB limit
            fileError = "The file size exceeds the 10MB limit and could not be shortened."
            raise serializers.ValidationError(fileError)
        return value

    class Meta:
        model = Song
        fields = [
            'id', 'user', 'is_user', 'title', 'updated_at',
            'created_at', 'audio_url', 'net_votes', 'artist_name',
            'link_to_song', 'audio_file', 'user_upvoted',
            'user_downvoted', 'user_vote_id'
        ]
