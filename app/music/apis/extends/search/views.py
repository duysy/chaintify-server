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
from .serializers import SearchSerializer


class SearchApiView(views.APIView):
    serializer_class = SearchSerializer

    def get(self, request, *args, **kwargs):
        text = request.query_params.get("text")
        if text != None:
            print("text : ", text)
            song = Song.objects.filter(name__contains=text, album__isPublic=True)[:5]
            artist = Artist.objects.filter(name__contains=text)[:5]
            album = Album.objects.filter(name__contains=text, isPublic=True)[:5]
            return Response({**{"song": list(song.values())},
                             **{"artist": list(artist.values())},
                             **{"album": list(album.values())}, })
        else:
            return Response({"error": "text not found"})
