from rest_framework import serializers

from .models import Post
from songs.models import Song


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    songs = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Song.objects.all(),
        required=False
    )

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
            'user', 'is_user', 'title', 'updated_at',
            'created_at', 'content', 'songs'
        ]
