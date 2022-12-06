from rest_framework.serializers import Serializer
from rest_framework import serializers

from ....models import Song


class SongSerializerPrivate(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'url', 'album', 'artist', 'name', 'cover', 'length', 'track', 'disc', 'lyrics', 'path', 'mtime', 'created_at', 'updated_at']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(SongSerializerPrivate, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)

class SongSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'url', 'album', 'artist', 'name', 'cover', 'length', 'track', 'disc', 'lyrics', 'path', 'mtime', 'created_at', 'updated_at']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(SongSerializerPublic, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)
