from django.db import models
from datetime import datetime

# Create your models here.
class Registered_Pathologist(models.Model):
    patho_id = models.AutoField(primary_key=True)
    pfirstname = models.CharField(max_length=150)
    pmiddlename = models.CharField(max_length=150)
    plastname = models.CharField(max_length=150)
    pdob = models.DateField()
    pmobile = models.IntegerField()
    pemail = models.CharField(max_length=70)
    ppassword = models.CharField(max_length=70)
    pconfirmpassword = models.CharField(max_length=70)
    pregistrationnumber = models.CharField(max_length=150)
    pregistrationcouncil = models.CharField(max_length=150)
    pvalidfrom = models.DateField(max_length=150)
    pvalidto = models.DateField(max_length=150)
    pstate = models.CharField(max_length=150)
    pdistrict = models.CharField(max_length=150)
    pcity = models.CharField(max_length=150)
    ppin = models.IntegerField()
    ptestfacility = models.CharField(max_length=150)
    pdatetime = models.DateTimeField(max_length=150)
    pathoflag = models.IntegerField()

