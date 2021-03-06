from django.contrib.gis import admin
from .models import ControlNode
from .models import ControlNodeUnit
from .models import ControlNodeType
from .models import ControlNodeData
from leaflet.admin import LeafletGeoAdmin

admin.site.register(ControlNode, LeafletGeoAdmin)
admin.site.register(ControlNodeUnit)
admin.site.register(ControlNodeType)
admin.site.register(ControlNodeData)
