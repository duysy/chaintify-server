from rest_framework.serializers import Serializer
from rest_framework import serializers


class ArtistSerializer(serializers.Serializer):
    name = serializers.CharField()
    cover = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        fields = ['name', 'cover', 'description']
