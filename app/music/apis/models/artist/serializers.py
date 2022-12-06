from rest_framework.serializers import Serializer
from rest_framework import serializers
from ....models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name',  'cover', 'description', 'created_at', 'updated_at']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(ArtistSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)
