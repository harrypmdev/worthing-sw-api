from django.urls import path

from venues import views

urlpatterns = [
    path("venues/", views.VenueList.as_view(), name="venue_list"),
    path("user_venues/", views.UserVenueList.as_view(), name="user_venue_list"),
    path("user_venues/<int:pk>/", views.UserVenueDetail.as_view()),
]
