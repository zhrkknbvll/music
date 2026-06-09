from django.urls import path
from .views import SongListCreateView
from .views import song_list


urlpatterns = [
    path('songs/', SongListCreateView.as_view()),
    path("", song_list),
]