from django.db import models

class BroadbandAppModel(models.Model):
     
     customerid=models.CharField(default="",max_length=50)
     customerName=models.CharField(default="",max_length=50)
     broadbandplan=models.CharField(default="",max_length=50)
     mobileNo=models.CharField(default="",max_length=50)
     subDate=models.CharField(default="",max_length=50)
     NxtSubDate=models.CharField(default="",max_length=50)
     amount=models.CharField(default="",max_length=50)
     address=models.CharField(default="",max_length=50)
     pincode=models.CharField(default="",max_length=50)
     ntwid=models.CharField(default="",max_length=50)
     
