from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):
    none = models.CharField(max_length=1000, blank=True)


class Artist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=True, null=True,)
    name = models.CharField(max_length=200, blank=True, null=True,)
    cover = models.CharField(max_length=200, blank=True, null=True,)
    description = models.CharField(max_length=500, blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,)
    artist = models.ManyToManyField(Artist)
    name = models.CharField(max_length=200)
    cover = models.CharField(max_length=200, blank=True, null=True,)
    description = models.TextField(null=True)
    isPublic = models.BooleanField(default=True)
    isMint = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Song(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True,)
    artist = models.ManyToManyField(Artist, blank=True, null=True,)
    name = models.CharField(max_length=200)
    cover = models.CharField(max_length=200, blank=True, null=True,)
    length = models.FloatField()
    track = models.IntegerField()
    disc = models.IntegerField()
    lyrics = models.TextField(blank=True, null=True,)
    path = models.CharField(max_length=200)
    mtime = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Interaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, blank=True, null=True,)
    liked = models.BooleanField()
    play_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True,)
    name = models.CharField(max_length=200)
    cover = models.CharField(max_length=200, blank=True, null=True,)
    song = models.ManyToManyField(Song, default=[])
    description = models.TextField(null=True)
    isPublic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
