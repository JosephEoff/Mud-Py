from django.contrib.gis.db import models

class Zone(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()

    boundary = models.PolygonField()
    
    def __str__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    zone = models.ForeignKey('zone.Zone',  on_delete=models.CASCADE, default=None, blank=True, null=True )
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.title

    
