from ....config import Config
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
import ipfshttpclient
import requests

from ....models import Album, Song
from .serializers import UpdateIsMintMetadataSerializer

from web3 import Web3
# BASE_GETAWAY = "http://127.0.0.1:8080/ipfs/"
BASE_GETAWAY = Config.BASE_GETAWAY
URL_API_IPFS = Config.URL_API_IPFS
ALCHEMY_KEY = Config.ALCHEMY_KEY
CHAINTIFY_CONTRACT_ADDRESS = Config.CHAINTIFY_CONTRACT_ADDRESS
RPC_URL = Config.RPC_URL

client = ipfshttpclient.connect(URL_API_IPFS)


class PinMetadata(views.APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        external_url = "Chaintify"

        try:
            dataAlbum = Album.objects.get(id=id)
        except:
            return Response({"status": "Album not found"})
        dataAlbum = model_to_dict(dataAlbum)
        dataAlbum["image"] = self.pinFile(dataAlbum["cover"])
        dataAlbum["external_url"] = external_url

        artistsModel = dataAlbum.pop("artist")
        artistArr = []
        for artist in artistsModel:
            artist_ = model_to_dict(artist)
            artist_["cover"] = self.pinFile(artist_["cover"])
            artistArr.append(artist_)
        dataAlbum["artist"] = artistArr

        dataSongModels = Song.objects.filter(album_id=id)
        songArr = []
        for dataSongModel in dataSongModels:
            song_ = model_to_dict(dataSongModel)
            song_["cover"] = self.pinFile(song_["cover"])
            song_["path"] = self.pinFile(song_["path"])
            artistsModel = song_.pop("artist")
            artistArr = []
            for artist in artistsModel:
                artist_ = model_to_dict(artist)
                artist_["cover"] = self.pinFile(artist_["cover"])
                artistArr.append(artist_)
            song_["artist"] = artistArr
            songArr.append(song_)

        del dataAlbum["id"]
        del dataAlbum["user"]
        del dataAlbum["cover"]
        del dataAlbum["isPublic"]
        del dataAlbum["isMint"]

        rep = {
            **dataAlbum,
            **{
                "song": songArr
            }
        }
        rep = self.pinJson(rep)
        return Response(rep)

    def pinFile(self, path):
        res = client.add(f"media/{path}")
        hash = res.get("Hash")
        full = f"{BASE_GETAWAY}/{hash}"
        return full

    def pinJson(self, json):
        hash = client.add_json(json)
        full = f"{BASE_GETAWAY}/{hash}"
        return {"uri": full}


class Metadata(views.APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        metadata = {}

        # url = f"https://polygon-mumbai.g.alchemy.com/nft/v2/{ALCHEMY_KEY}/getNFTMetadata?contractAddress={CHAINTIFY_CONTRACT_ADDRESS}&tokenId={id}&tokenType=ERC1155&refreshCache=false"
        # headers = {"accept": "application/json"}
        # response = requests.get(url, headers=headers)
        # metadata = response.json()
        # tokenUri = metadata["tokenUri"]["raw"]

        web3 = Web3(Web3.HTTPProvider(RPC_URL))
        address = Web3.toChecksumAddress(CHAINTIFY_CONTRACT_ADDRESS)
        abi = '[{"type":"function","name":"uri","constant":true,"stateMutability":"view","payable":false,"inputs":[{"type":"uint256","name":"id_"}],"outputs":[{"type":"string"}]}]'
        contract_instance = web3.eth.contract(address=address, abi=abi)
        tokenUri = contract_instance.functions.uri(id).call()
        try:
            response = requests.get(tokenUri)
            metadata["metadata"] = response.json()
        except Exception as ex:
            print(ex)

        return Response(metadata)


class UpdateIsMintMetadata(views.APIView):
    serializer_class = UpdateIsMintMetadataSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            try:
                dataAlbum = Album.objects.get(id=id)
                dataAlbum.isMint = True
                dataAlbum.save()
            except:
                return Response({"status": "Album not found"}, status=status.HTTP_404_NOT_FOUND)

            return Response({})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
