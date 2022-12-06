from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import routers, serializers, viewsets, views, status, mixins
from rest_framework.parsers import JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path, include
from django.forms.models import model_to_dict

from ...models import CustomUser
from .serializers import UploadSerializerPrivate
import random


class UploadAPIViewPrivate(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UploadSerializerPrivate
    base_media = "media"
    
    def post(self, request):
        serializer_class = UploadSerializerPrivate(data=request.data)
        if 'file_uploaded' not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            files = request.FILES.getlist('file_uploaded')
            for f in files:
                name = self.handle_uploaded_file(f)
            return Response({
                "status": "Success",
                "name": name
            }, status=status.HTTP_201_CREATED)

    def handle_uploaded_file(self, f):
        print(f.name, f.size)
        name = f.name
        first = name.split(".")[0]
        first = ''.join(e for e in first if e.isalnum())
        end = name.split(".")[-1]
        name = f"{first}{random.randint(1111111,9999999)}.{end}"
        with open(f"{self.base_media}/{name}", 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return name
class UploadAPIViewPublic(views.APIView):
    base_media = "media"
    def get(self, request):
        path = request.query_params.get("path")
        if path == None:
            return Response({})
        redirect_to = f'/{self.base_media}/{path}'
        return HttpResponseRedirect(redirect_to=redirect_to)

