from django.contrib import admin
from .models import Song, Favorite, ListeningHistory

admin.site.register(Song)
admin.site.register(Favorite)
admin.site.register(ListeningHistory)