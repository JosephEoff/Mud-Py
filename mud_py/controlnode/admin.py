from django.contrib.gis import admin
from .models import ControlNode
from .models import Note
from .models import ControlNodeUnit
from .models import ControlNodeDataType
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
admin.site.register(ControlNodeDataType)
admin.site.register(ControlNodeData)
