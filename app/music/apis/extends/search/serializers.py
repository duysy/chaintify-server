from rest_framework.serializers import Serializer
from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    name = serializers.CharField()

    class Meta:
        fields = ['name']
