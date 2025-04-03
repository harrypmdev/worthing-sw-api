"""Django serializers file that defines the serializer for the Post model."""

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post
from post_votes.models import PostVote
from followers.models import Follower


class PostSerializer(serializers.ModelSerializer):
    """Define the serializer for the Post model.

    Fields:
    user: serializers.ReadOnlyField -- redefines the user field as the
                                       user's username.
    user_id: serializers.ReadOnlyField -- the id of the connected User.
    profile_id: serializers.ReadOnlyField -- the profile id of the connected User, for use
                                             in the frontend's avatar component.
    user_image: serializers.ReadOnlyField -- the URL of the profile image of the connected User,
                                             for use in the frontend's avatar component.
    is_user: serializers.SerializerMethodField -- whether or not the Song belongs to
                                                  the currently authenticated User.
    user_upvoted: serializers.SerializerMethodField -- true if the current User has upvoted
                                                       this Post, false if not.
    user_downvoted: serializers.SerializerMethodField -- true if the current User has downvoted
                                                         this Post, false if not.
    user_vote_id: serializers.SerializerMethodField -- the id of the current User's vote if the
                                                       User has a vote for this Post. If the User
                                                       has no vote, is null.
    following_id: serializers.SerializerMethodField -- the id of the follower instance if the
                                                       current User is following the User who
                                                       created this Post. If the current User
                                                       is not following, is null.

    Methods:
    get_is_user -- a serializer get method for the is_user field.
    get_user_upvoted -- a serializer get method for the user_upvoted field.
    get_user_downvoted -- a serializer get method for the user_downvoted field.
    get_user_vote_id -- a serializer get method for the user_vote_id field.
    get_following_id -- a serializer get method for the following_id field.
    validate_content -- prevent the creation of posts with more than 400 characters.
    validate_title -- prevent the creation of posts with more than 50 characters in the title.

    A django serializer Meta class defines the fields and the related model.
    """

    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.pk")
    profile_id = serializers.ReadOnlyField(source="user.profile.id")
    user_image = serializers.ReadOnlyField(source="user.profile.image.url")
    is_user = serializers.SerializerMethodField()
    user_upvoted = serializers.SerializerMethodField()
    user_downvoted = serializers.SerializerMethodField()
    user_vote_id = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        """A serializer get method for the is_user field.
        Returns true if the Post belongs to the current User, false if not.
        """
        request = self.context["request"]
        return request.user == obj.user

    def get_user_upvoted(self, obj):
        """A serializer get method for the user_upvoted field.
        Returns true if the current User has upvoted this Post, false if not.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            return PostVote.objects.filter(post=obj, user=user, downvote=False).exists()
        return False

    def get_user_downvoted(self, obj):
        """A serializer get method for the user_downvoted field.
        Returns true if the current User has downvoted this Post, false if not.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            return PostVote.objects.filter(post=obj, user=user, downvote=True).exists()
        return False

    def get_user_vote_id(self, obj):
        """A serializer get method for the user_vote_id field.
        Returns the id of the current User's vote if the User has a vote for this Post.
        If the User has no vote, returns null.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            vote = PostVote.objects.filter(post=obj, user=user).first()
            return vote.id if vote else None
        return None

    def get_following_id(self, obj):
        """A serializer get method for the following_id field.
        Returns the id of the follower instance if the current User is following the User
        who created this Post. If the current User is not following, is null.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(user=user, followed=obj.user).first()
            return following.id if following else None
        return None

    def validate_content(self, value):
        """Prevent the creation of posts with more than 400 characters."""
        if len(value) > 400:
            raise ValidationError('Content exceeds the maximum length of 400 characters.')
        return value

    def validate_title(self, value):
        """Prevent the creation of posts with more than 50 characters in their title."""
        if len(value) > 50:
            raise ValidationError('Title exceeds the maximum length of 50 characters.')
        return value

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""

        model = Post
        fields = [
            "id",
            "user",
            "user_id",
            "user_image",
            "profile_id",
            "is_user",
            "title",
            "updated_at",
            "created_at",
            "content",
            "song",
            "net_votes",
            "user_upvoted",
            "user_downvoted",
            "user_vote_id",
            "following_id",
        ]
