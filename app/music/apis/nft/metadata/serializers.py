from rest_framework.serializers import Serializer
from rest_framework import serializers


class UpdateIsMintMetadataSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    class Meta:
        fields = ['id']
