"""Django serializers file that defines the serializer for the Song model."""

from rest_framework import serializers

from .models import Song
from song_votes.models import SongVote


class SongSerializer(serializers.ModelSerializer):
    """Define the serializer for the Song model.

    Fields:
    user: serializers.ReadOnlyField -- redefines the user field as the
                                       user's username.
    is_user: serializers.SerializerMethodField -- whether or not the Song belongs to
                                                  the currently authenticated User.
    user_upvoted: serializers.SerializerMethodField -- true if the current User has upvoted
                                                       this Song, false if not.
    user_downvoted: serializers.SerializerMethodField -- true if the current User has downvoted
                                                         this Song, false if not.
    user_vote_id: serializers.SerializerMethodField -- the id of the current User's vote if the
                                                       User has a vote for this Song. If the User
                                                       has no vote, is null.

    Methods:
    get_is_user -- a serializer get method for the is_user field.
    get_user_upvoted -- a serializer get method for the user_upvoted field.
    get_user_downvoted -- a serializer get method for the user_downvoted field.
    get_user_vote_id -- a serializer get method for the user_vote_id field.
    validate_audio_file -- a custom validation method to reject Song creation requests
                           with no file or a file over 10MB, the Cloudinary upload limit.

    A django serializer Meta class defines the fields and the related model.
    """

    user = serializers.ReadOnlyField(source="user.username")
    is_user = serializers.SerializerMethodField()
    user_upvoted = serializers.SerializerMethodField()
    user_downvoted = serializers.SerializerMethodField()
    user_vote_id = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        """A serializer get method for the is_user field.
        Returns true if the Song belongs to the current User, false if not.
        """
        request = self.context["request"]
        return request.user == obj.user

    def get_user_upvoted(self, obj):
        """A serializer get method for the user_upvoted field.
        Returns true if the current User has upvoted this Song, false if not.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            return SongVote.objects.filter(song=obj, user=user, downvote=False).exists()
        return False

    def get_user_downvoted(self, obj):
        """A serializer get method for the user_downvoted field.
        Returns true if the current User has downvoted this Song, false if not.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            return SongVote.objects.filter(song=obj, user=user, downvote=True).exists()
        return False

    def get_user_vote_id(self, obj):
        """A serializer get method for the user_vote_id field.
        Returns the id of the current User's vote if the User has a vote for this Song.
        If the User has no vote, returns null.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            vote = SongVote.objects.filter(song=obj, user=user).first()
            return vote.id if vote else None
        return None

    def validate_audio_file(self, value):
        """A custom validation method to reject Song creation requests with no file or
        a file over 10MB, the Cloudinary upload limit.
        """
        if not value:
            raise serializers.ValidationError("An audio file is required.")
        if value.size > 10 * 1024 * 1024:  # 10MB limit
            fileError = (
                "The file size exceeds the 10MB limit and could not be shortened."
            )
            raise serializers.ValidationError(fileError)
        return value

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""

        model = Song
        fields = [
            "id",
            "user",
            "is_user",
            "title",
            "updated_at",
            "created_at",
            "audio_url",
            "net_votes",
            "artist_name",
            "link_to_song",
            "audio_file",
            "user_upvoted",
            "user_downvoted",
            "user_vote_id",
        ]
