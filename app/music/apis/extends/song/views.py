from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, views, status, mixins, generics
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.urls import path, include
from django.forms.models import model_to_dict

from ....models import Song, Artist, Album
from .serializers import GetSongByArtistSerializer

from rest_framework import serializers
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"
        depth = 1


class GetSongByArtistView(views.APIView):
    serializer_class = GetSongByArtistSerializer

    def get(self, request, *args, **kwargs):
        id = request.query_params.get("id")
        if (id != None):
            # print(id)
            queryset = Song.objects.select_related("album").filter(artist=id)[:5]
            data = SongSerializer(queryset, many=True).data
            # print(list(data))
            return Response(list(data))
        return Response({"error": "id not found"})
