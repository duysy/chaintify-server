from django.contrib import admin

from .models import Album, Artist, Playlist, Song, Interaction, CustomUser
from import_export.admin import ImportExportMixin


class CustomUserAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


class CustomAlbum(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']


class CustomArtist(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']


class PlaylistAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


class SongAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name', 'album']


class InteractionAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.site_header = 'Chaintify administration'
admin.site.site_title = 'Chaintify administration'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Album, CustomAlbum)
admin.site.register(Artist, CustomArtist)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Interaction, InteractionAdmin)
