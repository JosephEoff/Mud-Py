from django.contrib.gis import admin
from .models import ControlNode
from leaflet.admin import LeafletGeoAdmin

admin.site.register(ControlNode, LeafletGeoAdmin)
