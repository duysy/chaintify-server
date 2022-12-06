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

from ...models import CustomUser
from .serializers import LoginSerializer


class AuthAPIView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        try:
            user = CustomUser.objects.get(username=request.user)
        except:
            return Response({"status": "Not Auth"})
        user = model_to_dict(user)
        return Response(user)

    def post(self, request):
        username = request.data.get('username')
        try:
            user = CustomUser.objects.get(username=username)
        except:
            return Response({"status": "Fail"})
        token, created = Token.objects.get_or_create(user_id=user.id)
        print(user)
        print(token, created)
        return Response({"token": token.key})

    def delete(self, request, pk=None):
        user = CustomUser.objects.get(username="admin")
        token, created = Token.objects.get_or_create(user_id=user.id)
        token.delete()
        return Response(status=status.HTTP_200_OK)
