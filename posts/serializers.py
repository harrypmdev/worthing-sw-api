from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    user_image = serializers.ReadOnlyField(source='user.profile.image.url')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'user_image', 'profile_id',
            'is_user', 'title', 'updated_at',
            'created_at', 'content', 'song', 'net_votes'
        ]
