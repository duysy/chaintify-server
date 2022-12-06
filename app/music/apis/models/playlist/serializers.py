from rest_framework.serializers import Serializer
from rest_framework import serializers
from ....models import Playlist


class PlaylistSerializerPrivate(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'user', 'name', 'cover', 'song', 'description', 'isPublic', 'created_at', 'updated_at']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(PlaylistSerializerPrivate, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)

    def create(self, validated_data):
        request = self.context.get('request', None)
        user = request.user

        playlist = Playlist.objects.create(**validated_data)
        playlist.user = user
        playlist.save()
        # print("playlist", model_to_dict(playlist))

        return playlist


class PlaylistSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'user', 'name', 'cover', 'song', 'description', 'isPublic', 'created_at', 'updated_at']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(PlaylistSerializerPublic, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)
