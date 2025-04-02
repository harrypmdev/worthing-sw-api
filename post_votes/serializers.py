from rest_framework import serializers

from .models import PostVote


class PostVoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context["request"]
        return request.user == obj.user

    class Meta:
        model = PostVote
        fields = [
            "id",
            "user",
            "is_user",
            "post",
            "created_at",
            "downvote",
        ]
