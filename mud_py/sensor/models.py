from django.contrib.gis.db import models


class SensorLocation(models.Model):
    location = models.PointField(default=None, blank=True, null=True)
    def __str__(self):
        return str(self.location.x) + ', ' + str(self.location.y)
        
class Sensor(models.Model):
    sensorID = models.CharField(max_length = 100)
    sensorLabel = models.CharField(max_length = 100,  null = True)
    controlnode = models.ForeignKey('controlnode.ControlNode',  related_name='assignedsensors',  on_delete=models.CASCADE,  default=None, blank=True, null=True)
    zone = models.ForeignKey('zone.Zone',  on_delete=models.CASCADE, default=None, blank=True, null=True )
    location= models.ForeignKey(SensorLocation,  on_delete=models.CASCADE,  blank = True,  null = True)
    
    def __str__(self):
        return self.sensorID
    
class Note(models.Model):
    title = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    timestamp = models.DateTimeField()
    sensor = models.ForeignKey('sensor.Sensor',  on_delete=models.CASCADE, default=None, blank=True, null=True )
    
    def __str__(self):
        return self.title

class SensorDataUnit(models.Model):
    name = models.CharField(max_length = 50)
    abbreviatedName = models.CharField(max_length = 5)
    
    def __str__(self):
        return self.name
        
class SensorDataType(models.Model):
    typeName = models.CharField(max_length = 50)
    unit = models.ForeignKey(SensorDataUnit,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.typeName
    
class SensorData(models.Model):
    sensor =  models.ForeignKey(Sensor,  on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    datatype = models.ForeignKey(SensorDataType,  on_delete=models.CASCADE)
    value = models.FloatField()
    zone = models.ForeignKey('zone.Zone',  on_delete=models.CASCADE, default=None, blank=True, null=True )
    location= models.ForeignKey(SensorLocation,  on_delete=models.CASCADE,  blank = True,  null = True)
    
    def __str__(self):
        return "Timestamp: " +str(self.timestamp) + " Type:" + str(self.datatype.typeName) + " Value:" + str(self.value) +  str(self.datatype.unit.abbreviatedName)
