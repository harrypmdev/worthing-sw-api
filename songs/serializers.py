from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Song
        fields = [
            'id', 'user', 'is_user', 'title', 'updated_at',
            'created_at', 'audio_url', 'net_votes', 'artist_name',
            'link_to_song', 'audio_file'
        ]
