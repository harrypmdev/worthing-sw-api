"""Django serializers file that defines the serializer for the Profile model."""

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """Define the serializer for the Profile model.

    Fields:
    user: serializers.ReadOnlyField -- redefines the user field as the
                                       user's username.
    user_id: serializers.ReadOnlyField -- the id of the related user.
    is_user: serializers.SerializerMethodField -- whether or not the Profile belongs to
                                                  the currently authenticated User.
    posts_count: serializers.ReadOnlyField -- the number of posts belonging to this profile.
    songs_count: serializers.ReadOnlyField -- the number of songs belonging to this profile.
    following_id: serializers.SerializerMethodField -- the id of the follower instance if the
                                                       current User is following the User
                                                       associated with this profile. If the
                                                       current User is not following, is null.
    followers_count: serializers.ReadOnlyField -- the number of users following this profile's
                                                  related user.
    following_count: serializers.ReadOnlyField -- the number of users the user related to this
                                                  profile is following.

    Methods:
    get_is_user -- a serializer get method for the is_user field.
    get_following_id -- a serializer get method for the is_following_id field.
    validate_bio -- prevent the creation of bios with more than 70 characters.
    """

    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.pk")
    is_user = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    songs_count = serializers.ReadOnlyField()
    following_id = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        """A serializer get method for the is_user field.
        Returns true if the Profile belongs to the current User, false if not.
        """
        request = self.context["request"]
        return request.user == obj.user

    def get_following_id(self, obj):
        """A serializer get method for the following_id field.
        Returns the id of the follower instance if the current User is following the User
        associated with this profile. If the current User is not following, returns null.
        """
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(user=user, followed=obj.user).first()
            return following.id if following else None
        return None

    def validate_bio(self, value):
        """Prevent the creation of bios with more than 70 characters."""
        if len(value) > 70:
            raise ValidationError("Bio exceeds the maximum length of 70 characters.")
        return value

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""

        model = Profile
        fields = [
            "id",
            "user",
            "user_id",
            "bio",
            "created_at",
            "image",
            "is_user",
            "following_id",
            "following_count",
            "followers_count",
            "posts_count",
            "songs_count",
        ]
