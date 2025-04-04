from django.contrib import admin

from .models import Venue, UserVenue

admin.site.register(Venue)
admin.site.register(UserVenue)
