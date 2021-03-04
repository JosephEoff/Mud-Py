from django.contrib.gis.db import models

class Zones(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    zonePolygon = models.PolygonField()
    #Need to link items into here somehow
