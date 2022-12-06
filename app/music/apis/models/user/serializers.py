from rest_framework.serializers import Serializer
from rest_framework import serializers
from ....models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'username', 'email', 'is_staff']
