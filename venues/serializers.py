"""Django serializers file that defines the serializers for the Venue and
UserVenue models.
"""


from rest_framework import serializers
from .models import Venue, UserVenue


class VenueSerializer(serializers.ModelSerializer):
    """Define the serializer for the Venue model.

    Fields:
    user_count: serializers.SerializerMethodField -- the number of Users
    connected to this Venue.

    Methods:
    get_user_count -- a serializer get method for the user_count field.

    A django serializer Meta class defines the fields and the related model.
    """
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        """A serializer get method for the user_count field.
        Returns the number of Users connected to this model via the UserVenue
        junction table.
        """
        return obj.venue_users.count()

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""
        model = Venue
        fields = ['id', 'name', 'user_count']


class UserVenueSerializer(serializers.ModelSerializer):
    """Define the serializer for the UserVenue model.

    Fields:
    user_name: serializers.ReadOnlyField -- the username of the linked user.
    name: serializers.ReadOnlyField - the name of the linked venue.
    user_count: serializers.SerializerMethodField -- the number of Users
    connected to the Venue this instance is linked to.

    Methods:
    get_user_count -- a serializer get method for the user_count field.

    A django serializer Meta class defines the fields and the related model.
    """
    user_name = serializers.ReadOnlyField(source="user.username")
    name = serializers.ReadOnlyField(source="venue.name")
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        """A serializer get method for the user_count field.
        Returns the number of Users connected to the Venue
        this instance is linked to.
        """
        return obj.venue.venue_users.count()

    class Meta:
        """Django serializer Meta class to define the fields and the related model."""
        model = UserVenue
        fields = [
            'id', 'user', 'venue', 'user_name', 'name',
            'user_count', 'created_at']
