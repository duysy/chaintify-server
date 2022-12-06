from rest_framework import routers
from .views import AuthAPIView
from django.contrib import admin
from django.urls import path, include,patterns


routerAuthViewSet = routers.DefaultRouter()

urlpatterns = patterns( [
    path(r'.', AuthAPIView.as_view()),
])
