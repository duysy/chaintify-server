from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, views
from rest_framework.response import Response

from .apis.auth.views import AuthAPIView
from .apis.file.views import UploadAPIViewPrivate, UploadAPIViewPublic

from .apis.models.urls import routerModelViewSet

# from .apis.extends.urls import routerExtendsViewSet
from .apis.extends.playlist.views import PlaylistUpdateSongApiView
from .apis.extends.album.views import AlbumUpdateSongApiView
from .apis.extends.artist.views import ArtistApiView
from .apis.nft.metadata.views import MetadataAlbum


class DocsView(views.APIView):
    def get(self, request, *args, **kwargs):
        apidocs = {
            'api/models/': request.build_absolute_uri('api/models/'),
            # 'api/extends/': request.build_absolute_uri('api/extends/'),
            'api/private/auth/': request.build_absolute_uri('api/private/auth/'),
            'api/private/upload/': request.build_absolute_uri('api/private/upload/'),
            'api/public/upload/': request.build_absolute_uri('api/public/upload/'),
            'api/private/extends/playlists': request.build_absolute_uri('api/private/extends/playlists'),
            'api/public/extends/albums/${id}': request.build_absolute_uri('api/public/extends/albums/1'),
            'api/private/extends/artists': request.build_absolute_uri('api/private/extends/artists'),
            'api/private/nft/metadata/<int:id>/': request.build_absolute_uri('api/private/nft/metadata/<int:id>/'),
        }
        return Response(apidocs)


urlpatterns = [
    # path(r'', TestView.as_view(), name="TestView"),
    path(r'', DocsView.as_view()),
    path(r'api/models/', include(routerModelViewSet.urls)),
    # path(r'api/extends/', include(routerExtendsViewSet.urls)),
    path(r'api/private/auth/', AuthAPIView.as_view()),
    path(r'api/private/upload/', UploadAPIViewPrivate.as_view()),
    path(r'api/public/upload/', UploadAPIViewPublic.as_view()),
    path(r'api/private/extends/playlists/', PlaylistUpdateSongApiView.as_view(), name='update_song_of_playlist'),
    path(r'api/public/extends/albums/<int:id>/', AlbumUpdateSongApiView.as_view(), name='get_album_by_id'),
    path(r'api/private/extends/artists/', ArtistApiView.as_view(), name='check_and_get_artist'),
    path(r'api/private/nft/metadata/<int:id>/', MetadataAlbum.as_view(), name='metadata_album'),
]
