from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import Song
from .serializers import SongSerializer
from django.shortcuts import render


class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @swagger_auto_schema(
        tags=["Music"],
        operation_description="Список и добавление песен"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Music"],
        operation_description="Добавить новую песню"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


def song_list(request):
    songs = Song.objects.all()
    return render(request, "music/song_list.html", {"songs": songs})



def song_list(request):
    query = request.GET.get("q")

    if query:
        songs = Song.objects.filter(title__icontains=query)
    else:
        songs = Song.objects.all()

    return render(
        request,
        "music/song_list.html",
        {
            "songs": songs,
            "query": query
        }
    )