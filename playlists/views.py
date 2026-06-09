from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import Playlist
from .serializers import PlaylistSerializer


class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    @swagger_auto_schema(
        tags=["Playlists"],
        operation_description="Создание и просмотр плейлистов"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Playlists"],
        operation_description="Создать плейлист"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)