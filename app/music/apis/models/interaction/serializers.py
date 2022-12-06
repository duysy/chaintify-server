from rest_framework.serializers import Serializer
from rest_framework import serializers
from ....models import Interaction


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ['id', 'url', 'user', 'song', 'liked', 'play_count', 'created_at', 'updated_at']
        # depth = 1

    def __init__(self, *args, **kwargs):
        super(InteractionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        self.Meta.depth = 0
        if request and request.method == 'GET':
            query_params = request.query_params
            if not query_params.get("depth") == None:
                depth = query_params.get("depth")
                self.Meta.depth = int(depth)
