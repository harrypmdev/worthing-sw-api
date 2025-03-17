from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'is_user', 'title', 'updated_at',
            'created_at', 'content', 'song', 'net_votes'
        ]
