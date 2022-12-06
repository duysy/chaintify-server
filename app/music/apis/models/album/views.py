from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import routers, serializers, viewsets, views, status, mixins
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.urls import path, include
from django.forms.models import model_to_dict

from ....models import Album
from .serializers import AlbumSerializerPrivate, AlbumSerializerPublic


class AlbumModelViewSetPrivate(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # queryset = Album.objects.all().order_by('-id')
    serializer_class = AlbumSerializerPrivate

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user=user).order_by('-id')


class AlbumModelViewSetPublic(viewsets.ModelViewSet):
    # queryset = Album.objects.all().order_by('-id')
    serializer_class = AlbumSerializerPublic

    def get_queryset(self):
        return Album.objects.filter(isPublic=True).order_by('-id')
