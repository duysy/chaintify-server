from rest_framework import routers
from django.urls import path, include
from .playlist.views import PlaylistViewSet

routerExtendsViewSet = routers.DefaultRouter()
