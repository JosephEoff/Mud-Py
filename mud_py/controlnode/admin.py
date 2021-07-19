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

class ControlNodeDataAdmin(admin.ModelAdmin):
     list_display  = ('timestamp', 'node',  'datatype',  'value')
    
admin.site.register(ControlNode, ControlNodeAdmin)
admin.site.register(ControlNodeUnit)
admin.site.register(ControlNodeDataType)
admin.site.register(ControlNodeData,  ControlNodeDataAdmin)
