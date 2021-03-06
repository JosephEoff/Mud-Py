from django.contrib.gis import admin
from .models import Zone
from leaflet.admin import LeafletGeoAdmin

#class ZoneAdmin(admin.OSMGeoAdmin):
#     map_info = True
#     map_width = 800
#     map_height = 600
#     num_zoom = 25
#     default_lon = 7.866667
#     default_lat = 49.85
     #layers = (
     #    ('maps', 1),
     #)


#admin.site.register(Zone, ZoneAdmin)
admin.site.register(Zone, LeafletGeoAdmin)
