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

from ....models import Artist, Song
from .serializers import ArtistSerializer


class ArtistApiView(views.APIView):
    serializer_class = ArtistSerializer

    def get(self, request):
        user = request.user
        try:
            data = Artist.objects.get(user=user)
        except:
            return Response({"status": "You not registry artist"}, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        return Response(model_to_dict(data))

    def post(self, request):
        user = request.user
        try:
            artistObject = request.data.dict()
            artistObject.pop("csrfmiddlewaretoken")
        except:
            artistObject = request.data
        try:
            artist = Artist.objects.get(user=user)
            artist.name = artistObject.get("name")
            artist.cover = artistObject.get("cover")
            artist.description = artistObject.get("description")
            artist.save()
        except:
            artist = Artist.objects.create(user=user, **artistObject)
            artist.save()

        return Response(model_to_dict(artist))
