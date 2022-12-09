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

import random
from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
w3 = Web3(Web3.HTTPProvider(""))


class AuthAPIView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def randomNone(self):
        return f"{random.randint(11111,999999)}"

    def get(self, request, format=None):
        try:
            user = CustomUser.objects.get(username=request.user)
        except:
            return Response({"status": "Not Auth"})
        user = model_to_dict(user)
        del user['password']
        return Response(user)

    def post(self, request):
        signature = request.data.get('signature')

        message = encode_defunct(text="hello")
        address = w3.eth.account.recover_message(message, signature=HexBytes(signature))
        print(address)

        try:
            user = CustomUser.objects.get(username=address)
        except:
            user = CustomUser.objects.create_user(username=address, password=self.randomNone(), none=self.randomNone())
        token, created = Token.objects.get_or_create(user_id=user.id)
        # print(user, token, created)
        return Response({"token": token.key})

    def delete(self, request, pk=None):
        username = request.user
        user = CustomUser.objects.get(username="username")
        token, created = Token.objects.get_or_create(user_id=user.id)
        token.delete()
        return Response(status=status.HTTP_200_OK)
