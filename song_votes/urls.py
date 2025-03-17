from django.urls import path

from song_votes import views

urlpatterns = [
    path('song_votes/', views.SongVoteList.as_view()),
    path('song_votes/<int:pk>/', views.SongVoteDetail.as_view()),
]
