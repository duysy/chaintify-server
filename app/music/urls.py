from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, views
from rest_framework.response import Response

from .apis.auth.views import AuthAPIView
from .apis.file.views import UploadAPIViewPrivate, UploadAPIViewPublic

from .apis.models.urls import routerModelViewSet

# from .apis.extends.urls import routerExtendsViewSet
from .apis.extends.playlist.views import PlaylistUpdateSongApiView
from .apis.extends.album.views import GetAlbumByIdApiViewPublic, GetAlbumByIdApiViewPrivate, GetAlbumByArtistApiView
from .apis.extends.artist.views import ArtistApiView
from .apis.extends.search.views import SearchApiView
from .apis.nft.metadata.views import PinMetadata, Metadata, UpdateIsMintMetadata
from .apis.nft.collection.views import Collection
from .apis.extends.song.views import GetSongByArtistView


class DocsView(views.APIView):
    def get(self, request, *args, **kwargs):
        apiDocs = {
            'api/models/': request.build_absolute_uri('api/models/'),
            # 'api/extends/': request.build_absolute_uri('api/extends/'),
            'api/private/auth/': request.build_absolute_uri('api/private/auth/'),
            'api/private/upload/': request.build_absolute_uri('api/private/upload/'),
            'api/public/upload/': request.build_absolute_uri('api/public/upload/'),
            'api/private/extends/playlists': request.build_absolute_uri('api/private/extends/playlists'),
            'api/public/extends/albums/${id}': request.build_absolute_uri('api/public/extends/albums/1'),
            'api/private/extends/albums/${id}': request.build_absolute_uri('api/private/extends/albums/1'),
            'api/private/extends/artists': request.build_absolute_uri('api/private/extends/artists'),
            'api/private/nft/pin-metadata/<int:id>/': request.build_absolute_uri('api/private/nft/pin-metadata/<int:id>/'),
            'api/private/nft/metadata/<int:id>/': request.build_absolute_uri('api/private/nft/metadata/<int:id>/'),
            'api/public/nft/collection/': request.build_absolute_uri('api/public/nft/collection/'),
            'api/private/nft/update-mint-nft/': request.build_absolute_uri('api/private/nft/update-mint-nft/'),
            'api/public/extends/search/': request.build_absolute_uri('api/public/extends/search/'),
            'api/public/extends/get-song-by-artist/': request.build_absolute_uri('api/public/extends/get-song-by-artist/'),
            'api/public/extends/get-album-by-artist/': request.build_absolute_uri('api/public/extends/get-album-by-artist/'),
        }
        return Response(apiDocs)


urlpatterns = [
    # path(r'', TestView.as_view(), name="TestView"),
    path(r'', DocsView.as_view()),
    path(r'api/models/', include(routerModelViewSet.urls)),
    # path(r'api/extends/', include(routerExtendsViewSet.urls)),
    path(r'api/private/auth/', AuthAPIView.as_view()),
    path(r'api/private/upload/', UploadAPIViewPrivate.as_view()),
    path(r'api/public/upload/', UploadAPIViewPublic.as_view()),
    path(r'api/private/extends/playlists/', PlaylistUpdateSongApiView.as_view(), name='update_song_of_playlist'),
    path(r'api/public/extends/albums/<int:id>/', GetAlbumByIdApiViewPublic.as_view(), name='get_album_by_id_public'),
    path(r'api/private/extends/albums/<int:id>/', GetAlbumByIdApiViewPrivate.as_view(), name='get_album_by_id_private'),
    path(r'api/private/extends/artists/', ArtistApiView.as_view(), name='check_and_get_artist'),
    path(r'api/private/nft/pin-metadata/<int:id>/', PinMetadata.as_view(), name='pin_metadata'),
    path(r'api/private/nft/metadata/<int:id>/', Metadata.as_view(), name='metadata'),
    path(r'api/public/nft/collection/', Collection.as_view(), name='collection'),
    path(r'api/private/nft/update-mint-nft/', UpdateIsMintMetadata.as_view(), name='update_mint_nft'),
    path(r'api/public/extends/search/', SearchApiView.as_view(), name='search'),
    path(r'api/public/extends/get-song-by-artist/', GetSongByArtistView.as_view(), name='get_song_by_artist'),
    path(r'api/public/extends/get-album-by-artist/', GetAlbumByArtistApiView.as_view(), name='get_album_by_artist'),
]
