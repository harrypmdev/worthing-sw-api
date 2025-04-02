from rest_framework import serializers

from .models import SongVote


class SongVoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context["request"]
        return request.user == obj.user

    class Meta:
        model = SongVote
        fields = [
            "id",
            "user",
            "is_user",
            "song",
            "created_at",
            "downvote",
        ]
