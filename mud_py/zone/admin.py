from django.contrib.gis import admin
from .models import Zone
from .models import Note
from leaflet.admin import LeafletGeoAdmin


class NoteInline(admin.StackedInline):
    model = Note

class ZoneAdmin(LeafletGeoAdmin):
    inlines = [
        NoteInline,
    ]

admin.site.register(Zone, ZoneAdmin)

