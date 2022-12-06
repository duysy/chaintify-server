from rest_framework.serializers import Serializer
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)

    class Meta:
        fields = ['username']