from django.contrib.gis import admin
from .models import Zones
from leaflet.admin import LeafletGeoAdmin

class ZonesAdmin(admin.OSMGeoAdmin): #LeafletGeoAdmin): #admin.OSMGeoAdmin):
     map_info = True
     map_width = 800
     map_height = 600
     num_zoom = 25
     default_lon = 7.866667
     default_lat = 49.85
     #layers = (
     #    ('maps', 1),
     #)


#admin.site.register(Zones, ZonesAdmin)
admin.site.register(Zones, LeafletGeoAdmin)
