from rest_framework.serializers import Serializer
from rest_framework import serializers


class AlbumUpdateSongSerializer(serializers.Serializer):
    song = serializers.IntegerField()

    class Meta:
        fields = ['song']
