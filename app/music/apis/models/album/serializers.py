from rest_framework.serializers import Serializer
from rest_framework import serializers
from ....models import Album
from django.forms.models import model_to_dict


class AlbumSerializerPrivate(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', "user", "artist", "name", "description", "cover", "isPublic", "created_at", "updated_at"]
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(AlbumSerializerPrivate, self).__init__(*args, **kwargs)
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
        artists = validated_data.pop("artist")
        album = Album.objects.create(**validated_data)
        album.user = user
        for artist in artists:
            album.artist.add(artist)
        album.save()
        return album


class AlbumSerializerPublic(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', "user", "artist", "name", "description", "cover", "isPublic", "created_at", "updated_at"]
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(AlbumSerializerPublic, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)