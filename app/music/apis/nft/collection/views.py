from ....config import Config
from .serializers import MetadataAlbumSerializer
from ....models import Album, Song
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
import random
from web3 import Web3
from hexbytes import HexBytes
w3 = Web3(Web3.HTTPProvider(""))


BASE_GETAWAY = Config.BASE_GETAWAY
URL_API_IPFS = Config.URL_API_IPFS
ALCHEMY_KEY = Config.ALCHEMY_KEY
CHAINTIFY_CONTRACT_ADDRESS = Config.CHAINTIFY_CONTRACT_ADDRESS
RPC_URL = Config.RPC_URL


class Collection(views.APIView):
    def get(self, request, *args, **kwargs):
        CHAINTIFY_OWNER_ADDRESS = request.query_params.get('address')
        if not CHAINTIFY_OWNER_ADDRESS == None:
            url = f"https://polygon-mumbai.g.alchemy.com/nft/v2/{ALCHEMY_KEY}/getNFTs?owner={CHAINTIFY_OWNER_ADDRESS}&pageSize=100&contractAddresses[]={CHAINTIFY_CONTRACT_ADDRESS}&withMetadata=true&&refreshCache=false&tokenUriTimeoutInMs=2000"
            print(url)
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            data = response.json()
            ownedNfts = data["ownedNfts"]
            ownedNftsArr = []
            for ownedNfts in ownedNfts:
                if ownedNfts.get("error") == "IPFS gateway timed out":
                    try:
                        tokenUri = ownedNfts["tokenUri"]["raw"]
                        metadata = requests.get(tokenUri)
                        ownedNfts["metadata"] = metadata.json()
                    except:
                        ownedNfts["metadata"] = {}

                # idHex = ownedNfts["id"]["tokenId"]
                # id = int(idHex, 0)
                # web3 = Web3(Web3.HTTPProvider(RPC_URL))
                # address = Web3.toChecksumAddress(CHAINTIFY_CONTRACT_ADDRESS)
                # abi = '[{"type":"function","name":"uri","constant":true,"stateMutability":"view","payable":false,"inputs":[{"type":"uint256","name":"id_"}],"outputs":[{"type":"string"}]}]'
                # contract_instance = web3.eth.contract(address=address, abi=abi)
                # tokenUri = contract_instance.functions.uri(id).call()
                # metadata = requests.get(tokenUri)
                # ownedNfts["metadata"] = metadata.json()

                ownedNftsArr.append(ownedNfts)
            return Response({"ownedNfts": ownedNftsArr})
        return Response({"error": "Address not found"})

    def post(self, request):
        return Response({})
