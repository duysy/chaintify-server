from rest_framework.serializers import Serializer
from rest_framework import serializers


class UploadSerializerPrivate(serializers.Serializer):
    file_uploaded = serializers.FileField(max_length=None, allow_empty_file=False)

    class Meta:
        fields = ['file_uploaded']