from django.urls import path

from post_votes import views

urlpatterns = [
    path("post_votes/", views.PostVoteList.as_view()),
    path("post_votes/<int:pk>/", views.PostVoteDetail.as_view()),
]
