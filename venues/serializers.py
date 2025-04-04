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
    user_id = serializers.ReadOnlyField(source="user.id")
    user = serializers.ReadOnlyField(source="user.username")
    venue_id = serializers.ReadOnlyField(source="user.id")
    name = serializers.ReadOnlyField(source="venue.name")
    user_count = serializers.SerializerMethodField()

    def get_user_count(self, obj):
        return obj.venue.venue_users.count()

    class Meta:
        model = UserVenue
        fields = [
            'id', 'user', 'user_id',
            'venue_id', 'name', 'user_count', 'created_at']
