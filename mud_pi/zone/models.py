from django.contrib.gis.db import models

class Zone(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    boundary = models.PolygonField()
    #Need to link items into here somehow
    
    def __str__(self):
        return self.name
