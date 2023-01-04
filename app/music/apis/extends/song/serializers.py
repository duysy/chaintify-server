from rest_framework.serializers import Serializer
from rest_framework import serializers


class GetSongByArtistSerializer(serializers.Serializer):
    id = serializers.CharField()

    class Meta:
        fields = ['id']
