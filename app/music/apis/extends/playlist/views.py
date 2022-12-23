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

from ....models import Playlist, Song
from .serializers import PlaylistUpdateSongSerializer


class PlaylistUpdateSongApiView(views.APIView):
    serializer_class = PlaylistUpdateSongSerializer

    def get(self, request, *args, **kwargs):
        data = Playlist.objects.all()
        return Response(list(data.values()))

    def post(self, request, *args, **kwargs):
        return Response({})
