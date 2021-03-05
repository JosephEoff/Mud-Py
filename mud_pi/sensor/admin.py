from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from .models import Sensor
from .models import SensorDataType
from .models import SensorDataUnit
from .models import SensorData
from leaflet.admin import LeafletGeoAdmin

gisadmin.site.register(Sensor, LeafletGeoAdmin)
admin.site.register(SensorDataUnit)
admin.site.register(SensorDataType)
admin.site.register(SensorData)
