from django.db import models

# Create your models here.
class Registered_Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, default="")
    username = models.CharField(max_length=250, default="")
    email = models.CharField(max_length=250, default="")
    password = models.CharField(max_length=250, default="")

class Patient_data(models.Model):
    patient_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(max_length=10)
    fulladdress = models.CharField(max_length=100)
    gender = models.IntegerField(max_length=5)
    chestpaintype = models.CharField(max_length=100)
    glucosevalue = models.CharField(max_length=100)
    bloodpressure = models.IntegerField(max_length=15)
    insulinvalue = models.IntegerField(max_length=20)
    bmi = models.CharField(max_length=50)
    prediabetic = models.CharField(max_length=100)
    dpf = models.CharField(max_length=100)
    cholestrol = models.CharField(max_length=100)
    dailyexercise = models.CharField(max_length=15)
    sleepinghabits = models.CharField(max_length=100)
    brushinghabits = models.CharField(max_length=100)