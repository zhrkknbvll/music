from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Music API",
        default_version="v1",
        description="Music API Documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("docs/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),

    path("api/users/", include("users.urls")),
    path("api/music/", include("music.urls")),
    path("api/playlists/", include("playlists.urls")),

    path("", include("music.urls")),
    ]