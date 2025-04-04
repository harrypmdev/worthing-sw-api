from django.urls import path

from venues import views

urlpatterns = [
    path("venues/", views.VenueList.as_view()),
    path("user_venues/", views.UserVenueList.as_view()),
    path("user_venues/<int:pk>/", views.UserVenueDetail.as_view()),
]
