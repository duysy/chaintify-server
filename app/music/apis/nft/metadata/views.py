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

from ....models import Album, Song
from .serializers import MetadataAlbumSerializer


class MetadataAlbum(views.APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            dataAlbum = Album.objects.get(id=id)
        except:
            return Response({"status": "Album not found"})
        dataAlbum = model_to_dict(dataAlbum)
        dataAlbum["image"] = dataAlbum["cover"]
        dataAlbum["external_url"] = "Chaintify"
        
        artistsModel = dataAlbum.pop("artist")

        dataAlbum["artist"] = [model_to_dict(artist) for artist in artistsModel]

        dataSongModels = Song.objects.filter(album_id=id)
        songArr = []
        for dataSongModel in dataSongModels:
            song = model_to_dict(dataSongModel)
            artistsModel = song.pop("artist")
            song["artist"] = [model_to_dict(artist) for artist in artistsModel]
            songArr.append(song)

        
        del dataAlbum["id"]
        del dataAlbum["user"]
        del dataAlbum["cover"]
        del dataAlbum["isPublic"]

        rep = {
            **dataAlbum,
            **{
                "song": songArr
            }
        }

        return Response(rep)

    def post(self, request):
        return Response({})
