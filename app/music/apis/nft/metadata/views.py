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


# BASE_GETAWAY = "http://127.0.0.1:8080/ipfs/"
BASE_GETAWAY = "https://5955-2001-ee0-4b47-a640-2d5f-5aea-a537-9304.ap.ngrok.io/ipfs"
URL_API_IPFS = "/ip4/127.0.0.1/tcp/5001"

ALCHEMY_KEY = "HxETu9kBk_Uvs5LkdMCwvK-2KqV3Eg3i"
CHAINTIFY_CONTRACT_ADDRESS = "0x09f2738264Bd8e8076102f2a010523a60BcE5648"
CHAINTIFY_ADDRESS_OWNER = "0x71CB05EE1b1F506fF321Da3dac38f25c0c9ce6E1"

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
        url = f"https://polygon-mumbai.g.alchemy.com/nft/v2/{ALCHEMY_KEY}/getNFTMetadata?contractAddress={CHAINTIFY_CONTRACT_ADDRESS}&tokenId={id}&tokenType=ERC1155&refreshCache=true"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        return Response(response.json())


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
                return Response({"status": "Album not found"})

            return Response({})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
