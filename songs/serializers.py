from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Song
        fields = [
            'user', 'title', 'updated_at', 'created_at',
            'audio_file', 'artist_name', 'duration', 'posts'
        ]
