from django.contrib.gis.db import models

class ControlNode(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    zone = models.ForeignKey('zone.Zone',  on_delete=models.CASCADE)
    location = models.PointField()
    
    def __str__(self):
        return self.name
        
class ControlNodeUnit(models.Model):
    name = models.CharField(max_length = 50)
    abbreviatedName = models.CharField(max_length = 5)
    
    def __str__(self):
        return self.name
        
class ControlNodeType(models.Model):
    typeName = models.CharField(max_length = 50)
    unit = models.ForeignKey(ControlNodeUnit,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.typeName
    
class ControlNodeData(models.Model):
    sensor =  models.ForeignKey(ControlNode,  on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    datatype = models.ForeignKey(ControlNodeType,  on_delete=models.CASCADE)
    value = models.FloatField()
    
    def __str__(self):
        return "Timestamp: " +str(self.timestamp) + " Type:" + str(self.datatype.typeName) + " Value:" + str(self.value) +  str(self.datatype.unit.abbreviatedName)
