from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType

from .models import Vote
from posts.models import Post


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    base_content = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user

    def get_base_content(self, obj):
        if obj.base_content:
            return {
                'id': obj.base_content.id,
                'type': 'post' if isinstance(obj.base_content, Post) else 'song'
            }
        return None

    def create(self, validated_data):
        content_type = validated_data.pop('content_type')
        object_id = validated_data.pop('object_id')
        content_type = ContentType.objects.get(model=content_type)
        base_content = content_type.get_object_for_this_type(pk=object_id)
        return Vote.objects.create(base_content=base_content, **validated_data)

    class Meta:
        model = Vote
        fields = [
            'user', 'is_user', 'base_content', 'content_type', 'object_id'
        ]
