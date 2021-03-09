from django.contrib.gis import admin
from .models import ControlNode
from .models import Note
from .models import ControlNodeUnit
from .models import ControlNodeType
from .models import ControlNodeData
from leaflet.admin import LeafletGeoAdmin

class NoteInline(admin.TabularInline):
    model = Note

class ControlNodeAdmin(LeafletGeoAdmin):
    inlines = [
        NoteInline,
    ]

admin.site.register(ControlNode, ControlNodeAdmin)
admin.site.register(ControlNodeUnit)
admin.site.register(ControlNodeType)
admin.site.register(ControlNodeData)
