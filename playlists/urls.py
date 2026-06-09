from django.urls import path
from .views import PlaylistListCreateView

urlpatterns = [
    path("", PlaylistListCreateView.as_view()),

]