from django.contrib.gis.db import models

class ControlNode(models.Model):
    nodeid = models.CharField(max_length = 100)
    description = models.TextField(blank=True) 
    location = models.PointField(default=None, blank=True, null=True)
    
    def __str__(self):
        return self.nodeid
    
class Note(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    controlnode = models.ForeignKey('controlnode.ControlNode',  on_delete=models.CASCADE, default=None, blank=True, null=True )
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.title

class ControlNodeUnit(models.Model):
    name = models.CharField(max_length = 50)
    abbreviatedName = models.CharField(max_length = 5)
    
    def __str__(self):
        return self.name
        
class ControlNodeDataType(models.Model):
    typeName = models.CharField(max_length = 50)
    unit = models.ForeignKey(ControlNodeUnit,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.typeName
    
class ControlNodeData(models.Model):
    sensor =  models.ForeignKey(ControlNode,  on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    datatype = models.ForeignKey(ControlNodeDataType,  on_delete=models.CASCADE)
    value = models.FloatField()
    
    def __str__(self):
        return "Timestamp: " +str(self.timestamp) + " Type:" + str(self.datatype.typeName) + " Value:" + str(self.value) +  str(self.datatype.unit.abbreviatedName)
