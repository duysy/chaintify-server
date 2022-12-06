from rest_framework.serializers import Serializer
from rest_framework import serializers


class PlaylistUpdateSongSerializer(serializers.Serializer):
    song = serializers.IntegerField()

    class Meta:
        fields = ['song']
