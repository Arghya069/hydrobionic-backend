from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hydb(models.Model):
    device_id=models.TextField(max_length=30,primary_key=True)
    temp=models.FloatField(null=False,default=0.0)
    temp_w=models.FloatField(null=False,default=0.0)
    humid=models.IntegerField(null=False,default=0)
    w_level=models.IntegerField(null=False,default=0)
    pump=models.IntegerField(null=False,choices=((0,0),(1,1)),default=0)
    def __str__(self):
        return self.device_id
        
class UserDevices(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    device_id = models.ForeignKey(Hydb,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +' : '+self.device_id.device_id

    