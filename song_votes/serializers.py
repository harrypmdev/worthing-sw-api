"""Django serializers file that defines the serializer for the SongVote model."""

from rest_framework import serializers

from .models import SongVote


class SongVoteSerializer(serializers.ModelSerializer):
    """Define the serializer for the SongVote model.

    Fields:
    user: serializers.ReadOnlyField -- redefines the user field as the
                                        user's username.
    is_user: serializers.SerializerMethodField -- whether or not the SongVote belongs to
                                                    the currently authenticated User.

    Methods:
    get_is_user -- a serializer get method for the is_user field.

    A django serializer Meta class defines the fields and the related model.
    """

    user = serializers.ReadOnlyField(source="user.username")
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        """A serializer get method for the is_user field.
        Returns true if the Song belongs to the current User, false if not.
        """
        request = self.context["request"]
        return request.user == obj.user

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""

        model = SongVote
        fields = [
            "id",
            "user",
            "is_user",
            "song",
            "created_at",
            "downvote",
        ]
