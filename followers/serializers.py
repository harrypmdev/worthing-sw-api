"""Django serializers file that defines the serializer for the Follower model."""

from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """Define the serializer for the Follower model.

    Fields:
    user: serializers.ReadOnlyField -- redefines the user field as the user's username.
    user_id: serializers.ReadOnlyField -- the id of the connected User.
    followed_name: serializers.ReadOnlyField -- the username of the user that is being followed.

    Methods:
    create -- overwrites the default create method to check for possible duplicate followers before
              follower creation.

    A django serializer Meta class defines the fields and the related model.
    """

    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.pk")
    followed_name = serializers.ReadOnlyField(source="followed.username")

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""

        model = Follower
        fields = ["id", "user", "followed", "followed_name", "created_at", "user_id"]

    def create(self, validated_data):
        """Overwrite the default create method to check for possible duplicate followers before
        follower creation.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({"detail": "possible duplicate"})
