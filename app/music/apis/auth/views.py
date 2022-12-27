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
import string
from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct
w3 = Web3(Web3.HTTPProvider(""))


class AuthAPIView(views.APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def getNoneMessage(self, address):
        none = self.randomString()
        return f'''
Welcome to Chaintify!

This request will not trigger a blockchain transaction or cost any gas fees.

Your authentication status will reset after login later.

Wallet address: {address}

None : {none}
''' 

    def randomString(self, n=30):
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=n))

    def get(self, request, *args, **kwargs):
        address = request.query_params.get('address')
        none = self.getNoneMessage(address=address)
        try:
            user = CustomUser.objects.get(username=address)
            user.none = none
            user.save()
        except:
            user = CustomUser.objects.create_user(username=address, password=self.randomString(n=14), none=none)
        return Response({"none": user.none, "address": user.username})

    def post(self, request):
        signature = request.data.get('signature')
        none = request.data.get('none')
        message = encode_defunct(text=none)
        address = w3.eth.account.recover_message(message, signature=HexBytes(signature))
        try:
            user = CustomUser.objects.get(username=address)
            token, _ = Token.objects.get_or_create(user_id=user.id)
            print(user, token, address)
            return Response({"token": token.key, "address": address})
        except:
            return Response({"error": "not found"})

    def delete(self, request, pk=None):
        username = request.user
        user = CustomUser.objects.get(username="username")
        token, created = Token.objects.get_or_create(user_id=user.id)
        token.delete()
        return Response(status=status.HTTP_200_OK)
