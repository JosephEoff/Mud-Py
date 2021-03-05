from django.contrib.gis.db import models

class ControlNode(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    zone = models.ForeignKey('zone.Zone',  on_delete=models.CASCADE)
    location = models.PointField()
    
    def __str__(self):
        return self.name
