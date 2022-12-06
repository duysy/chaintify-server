from rest_framework import routers

from .user.views import UserModelViewSet
from .album.views import AlbumModelViewSetPrivate, AlbumModelViewSetPublic
from .artist.views import ArtistModelViewSet
from .interaction.views import InteractionModelViewSet
from .playlist.views import PlaylistModelViewSetPrivate, PlaylistModelViewSetPublic
from .song.views import SongModelViewSetPublic, SongModelViewSetPrivate


routerModelViewSet = routers.DefaultRouter()
routerModelViewSet.register(r'users', UserModelViewSet)
routerModelViewSet.register(r'artists', ArtistModelViewSet, basename="model-artists")
routerModelViewSet.register(r'interactions', InteractionModelViewSet)

routerModelViewSet.register(r'private/albums', AlbumModelViewSetPrivate, basename="model-albums-private")
routerModelViewSet.register(r'private/playlists', PlaylistModelViewSetPrivate, basename="model-playlists-private")
routerModelViewSet.register(r'private/songs', SongModelViewSetPrivate, basename="model-song-private")

routerModelViewSet.register(r'public/albums', AlbumModelViewSetPublic, basename="model-albums-public")
routerModelViewSet.register(r'public/playlists', PlaylistModelViewSetPublic, basename="model-playlists-public")
routerModelViewSet.register(r'public/songs', SongModelViewSetPublic)


# base name just for model hipelink
