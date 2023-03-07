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


class GetAlbumByIdApiViewPublic(views.APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            dataAlbum = Album.objects.get(id=id, isPublic=True)
        except:
            return Response({"status": "Album not found"})
        dataAlbum = model_to_dict(dataAlbum)

        artistsModel = dataAlbum.pop("artist")
        dataAlbum["artist"] = [model_to_dict(artist) for artist in artistsModel]

        dataSongModels = Song.objects.filter(album_id=id)
        songArr = []
        for dataSongModel in dataSongModels:
            song = model_to_dict(dataSongModel)
            artistsModel = song.pop("artist")
            song["artist"] = [model_to_dict(artist) for artist in artistsModel]
            songArr.append(song)

        rep = {
            **dataAlbum,
            **{
                "song": songArr
            }
        }
        return Response(rep)

    def post(self, request):
        return Response({})


class GetAlbumByIdApiViewPrivate(views.APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        user = self.request.user
        try:
            dataAlbum = Album.objects.get(user=user, id=id)
        except:
            return Response({"status": "Album not found"}, status=status.HTTP_404_NOT_FOUND)
        dataAlbum = model_to_dict(dataAlbum)

        artistsModel = dataAlbum.pop("artist")
        dataAlbum["artist"] = [model_to_dict(artist) for artist in artistsModel]

        dataSongModels = Song.objects.filter(album_id=id)
        songArr = []
        for dataSongModel in dataSongModels:
            song = model_to_dict(dataSongModel)
            artistsModel = song.pop("artist")
            song["artist"] = [model_to_dict(artist) for artist in artistsModel]
            songArr.append(song)

        rep = {
            **dataAlbum,
            **{
                "song": songArr
            }
        }
        return Response(rep)

    def post(self, request):
        return Response({})


class GetAlbumByArtistApiView(views.APIView):

    def get(self, request, *args, **kwargs):
        id = request.query_params.get("id")
        if (id != None):
            print(id)
            album = Album.objects.filter(artist=id, isPublic=True)[:5]
            # print(list(album.values()))
            return Response(list(album.values()))
        return Response({"error": "id not found"}, status=status.HTTP_404_NOT_FOUND)
