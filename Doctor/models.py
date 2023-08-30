from django.db import models
from datetime import datetime


# Create your models here.
class Registered_Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True, serialize=False, auto_created=True)
    dfirstname = models.CharField(max_length=150)
    dmiddlename = models.CharField(max_length=150)
    dlastname = models.CharField(max_length=150)
    ddob = models.CharField(max_length=150)
    dmobile = models.IntegerField()
    demail = models.CharField(max_length=50)
    dpassword = models.CharField(max_length=150)
    dconfirmpassword = models.CharField(max_length=150)
    dregistrationcouncil = models.CharField(max_length=150)
    dothercouncil = models.CharField(max_length=150, default=None)
    dregistrationnumber = models.CharField(max_length=150)
    dqualification = models.CharField(max_length=70)
    duniversityname = models.CharField(max_length=150)
    dpassingyear = models.IntegerField()
    dclinicname = models.CharField(max_length=150)
    dstate = models.CharField(max_length=150)
    ddistrict = models.CharField(max_length=200)
    dcity = models.CharField(max_length=200)
    dpincode = models.IntegerField()
    dtestfacility = models.CharField(max_length=150)
    ddatetime = models.DateTimeField(max_length=50, blank=True, null=True)
    doctorflag = models.IntegerField()
