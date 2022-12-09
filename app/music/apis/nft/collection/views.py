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
import requests

from ....models import Album, Song
from .serializers import MetadataAlbumSerializer

ALCHEMY_KEY = "HxETu9kBk_Uvs5LkdMCwvK-2KqV3Eg3i"
CHAINTIFY_CONTRACT_ADDRESS = "0xeb7d600371C4a7790f822B02b7Bfc05900884EAb"
CHAINTIFY_OWNER_ADDRESS = "0xC85C795D69e67De78B02ccAA51F03f4c56B2446e"


class Collection(views.APIView):
    def get(self, request, *args, **kwargs):
        CHAINTIFY_OWNER_ADDRESS = request.query_params.get('address')
        if not CHAINTIFY_OWNER_ADDRESS == None:
            url = f"https://polygon-mumbai.g.alchemy.com/nft/v2/{ALCHEMY_KEY}/getNFTs?owner={CHAINTIFY_OWNER_ADDRESS}&pageSize=100&contractAddresses[]={CHAINTIFY_CONTRACT_ADDRESS}&withMetadata=true&&refreshCache=true&tokenUriTimeoutInMs=5000"
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            return Response(response.json())
        return Response({"error": "Address not found"})

    def post(self, request):
        return Response({})
