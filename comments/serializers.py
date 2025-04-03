"""Django serializers file that defines the serializer for the Comment model."""

from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Define the serializer for the Comment list View.

    Fields:
    user: serializers.ReadOnlyField -- redefines the user field as the
                                       user's username.
    profile_id: serializers.ReadOnlyField -- the profile id of the connected User, for use
                                             in the frontend's avatar component.
    profile_image: serializers.ReadOnlyField -- the URL of the profile image of the connected User,
                                                for use in the frontend's avatar component.
    is_user: serializers.SerializerMethodField -- whether or not the Song belongs to
                                                  the currently authenticated User.
    created_at: serializers.SerializerMethodField -- the date and time of the Comments creation,
                                                     converted to natural time for easy reading.
    updated_at: serializers.SerializerMethodField -- the date and time of the Comments last update,
                                                     converted to natural time for easy reading.


    Methods:
    get_is_user -- a serializer get method for the is_user field.
    get_created_at -- a serializer get method for the created_at field.
    get_updated_at -- a serializer get method for the updated_at field.
    validate_content -- prevent the creation of comments with more than 300 characters.

    A django serializer Meta class defines the fields and the related model.
    """

    user = serializers.ReadOnlyField(source="user.username")
    profile_id = serializers.ReadOnlyField(source="user.profile.id")
    profile_image = serializers.ReadOnlyField(source="user.profile.image.url")
    is_user = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        """A serializer get method for the is_user field.
        Returns true if the Post belongs to the current User, false if not.
        """
        request = self.context["request"]
        return request.user == obj.user

    def get_created_at(self, obj):
        """A serializer get method for the get_created_at field.
        Returns the date and time in natural time for easy reading.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """A serializer get method for the get_updated_at field.
        Returns the date and time in natural time for easy reading.
        """
        return naturaltime(obj.updated_at)

    def validate_content(self, value):
        if len(value) > 300:
            raise ValidationError('Content exceeds the maximum length of 300 characters.')
        return value

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""

        model = Comment
        fields = [
            "id",
            "user",
            "profile_id",
            "profile_image",
            "is_user",
            "created_at",
            "updated_at",
            "content",
            "post",
        ]


class CommentDetailSerializer(CommentSerializer):
    """Define the serializer for the Comment detail view.

    Fields:
    post: serializers.ReadOnlyField - Defines the post field as the id of the existing post,
                                      so PUT requests do not need to provide it.
    """

    post = serializers.ReadOnlyField(source="post.id")
