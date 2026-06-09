from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)

    audio_file = models.FileField(upload_to='songs/')
    cover = models.ImageField(upload_to='covers/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'song')


class ListeningHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE
    )

    listened_at = models.DateTimeField(
        auto_now_add=True
    )