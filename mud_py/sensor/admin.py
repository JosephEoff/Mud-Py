from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from .models import Sensor
from .models import Note
from .models import SensorDataType
from .models import SensorDataUnit
from .models import SensorData
from .models import SensorLocation
from leaflet.admin import LeafletGeoAdmin


class NoteInline(admin.StackedInline):
    model = Note

class SensorAdmin(LeafletGeoAdmin):
    inlines = [
        NoteInline,
    ]
    list_display  = ('sensorLabel','sensorID', 'controlnode', 'zone')

class SensorLocationAdmin(LeafletGeoAdmin):
    list_display  = ('location', )

class SensorDataAdmin(admin.ModelAdmin):    
    list_display  = ('timestamp', 'sensor', 'zone',  'datatype',  'value')

gisadmin.site.register(Sensor, SensorAdmin)
admin.site.register(SensorDataUnit)
admin.site.register(SensorDataType)
admin.site.register(SensorData,  SensorDataAdmin)
admin.site.register(SensorLocation,  SensorLocationAdmin)
