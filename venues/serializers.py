from rest_framework import serializers
from .models import Venue, UserVenue


class VenueSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        return obj.venue_users.count()

    class Meta:
        model = Venue
        fields = ['id', 'name', 'user_count']


class UserVenueSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source="user.username")
    name = serializers.ReadOnlyField(source="venue.name")
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        return obj.venue.venue_users.count()

    class Meta:
        model = UserVenue
        fields = [
            'id', 'user', 'venue', 'user_name', 'name',
            'user_count', 'created_at']
