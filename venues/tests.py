from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from venues import models


class TestUserCount(TestCase):
    """Tests for the Venue and UserVenue user_count fields."""

    def setUp(self):
        self.user = User.objects.create(username="existingUser", email="test@gmail.com")
        self.user.set_password("userPassword123%")
        self.user.save()
        self.user_two = User.objects.create(username="existingUserTwo", email="test@gmail.com")
        self.user_two.set_password("userPassword123%")
        self.user.save()
        self.venue = models.Venue.objects.create(name="The Broadwater Pub")
        self.venue.save()

    def test_no_user_count_to_start(self):
        """Test that with no UserVenue instances, user_count is to start 0 for a Venue."""
        response = self.client.get(reverse("venue_list"))
        user_count = response.json()['results'][0]['user_count']
        self.assertEqual(user_count, 0, msg="User count was not equal to 0")

    def test_venue_user_count_updates(self):
        """Test that when 2 UserVenues are added, the Venue user_count updates."""
        user_venue_one = models.UserVenue.objects.create(user=self.user, venue=self.venue)
        user_venue_one.save()
        user_venue_two = models.UserVenue.objects.create(user=self.user_two, venue=self.venue)
        user_venue_two.save()
        response = self.client.get(reverse("venue_list"))
        user_count = response.json()["results"][0]["user_count"]
        self.assertEqual(user_count, 2, msg="User count was not equal to 2")

    def test_user_venue_user_count_updates(self):
        """Test that when 2 UserVenues are added, the user_count of both UserVenues is 2."""
        user_venue_one = models.UserVenue.objects.create(user=self.user, venue=self.venue)
        user_venue_one.save()
        user_venue_two = models.UserVenue.objects.create(user=self.user_two, venue=self.venue)
        user_venue_two.save()
        response = self.client.get(reverse("user_venue_list"))
        user_count_one = response.json()["results"][0]["user_count"]
        user_count_two = response.json()["results"][1]["user_count"]
        self.assertEqual(user_count_one, 2, msg="User count was not equal to 2")
        self.assertEqual(user_count_two, 2, msg="User count was not equal to 2")
