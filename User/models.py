from django.db import models
from Manager.models import Patient_data
from datetime import datetime

# Create your models here.
class watch_data(models.Model):
    patient_id = models.IntegerField()
    steps = models.CharField(max_length=50)
    calories_burnt = models.CharField(max_length=50)
    heart_minutes = models.CharField(max_length=50)
    date = models.DateField(default=None)
    # date = models.CharField(max_length=50)

    class Meta:
        ordering = ['date']

class vitals_data(models.Model):
    vid = models.AutoField(primary_key=True)
    bodytemperature = models.IntegerField()
    pulserate = models.CharField(max_length=50)
    respiratoryrate = models.CharField(max_length=50)
    bp = models.CharField(max_length=50)
    spo2 = models.IntegerField()
    weight = models.CharField(max_length=50)
    bloodsugarfbs = models.CharField(max_length=50)
    bloodsugarrbs = models.CharField(max_length=50)
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    class Meta:
        ordering = ['datetime']
        unique_together = (('datetime', 'vid', 'patient_id'),)

class health_condition_data(models.Model):
    hcid = models.AutoField(primary_key=True)
    diabetes = models.CharField(max_length=50, default=None, null=True, blank=True)
    obesity = models.CharField(max_length=50, default=None, null=True, blank=True)
    cancer = models.CharField(max_length=50, default=None, null=True, blank=True)
    heart_disease = models.CharField(max_length=50, default=None, null=True, blank=True)
    stroke = models.CharField(max_length=50, default=None, null=True, blank=True)
    mental_health = models.CharField(max_length=50, default=None, null=True, blank=True)
    asthama = models.CharField(max_length=50, default=None, null=True, blank=True)
    hearing_loss = models.CharField(max_length=50, default=None, null=True, blank=True)
    arthritis = models.CharField(max_length=50, default=None, null=True, blank=True)
    post_traumatic_stress_disorder = models.CharField(max_length=50, default=None, null=True, blank=True)
    hiv_aids = models.CharField(max_length=50, default=None, null=True, blank=True)
    gastrointestinal_disorder = models.CharField(max_length=50, default=None, null=True, blank=True)
    datetime = models.DateTimeField()
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)

    class Meta:
        ordering = ['datetime']
        unique_together = (('hcid', 'datetime', 'patient_id'))

class todays_feel_data(models.Model):
    today_id = models.AutoField(primary_key=True)
    bodyache_duration = models.CharField(max_length=20)
    bodyache_occurance = models.CharField(max_length=20)
    allergy_duration = models.CharField(max_length=20)
    allergy_occurance = models.CharField(max_length=20)
    backpain_duration = models.CharField(max_length=20)
    backpain_occurance = models.CharField(max_length=20)
    headache_duration = models.CharField(max_length=20)
    headache_occurance = models.CharField(max_length=20)
    dental_pain_duration = models.CharField(max_length=20)
    dental_pain_occurance = models.CharField(max_length=20)
    acidity_duration = models.CharField(max_length=20)
    acidity_occurance = models.CharField(max_length=20)
    stomachache_duration = models.CharField(max_length=20)
    stomachache_occurance = models.CharField(max_length=20)
    common_cold_duration = models.CharField(max_length=20)
    common_cold_occurance = models.CharField(max_length=20)
    vomiting_duration = models.CharField(max_length=20)
    vomiting_occurance = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)

    class Meta:
        ordering = ['datetime']
        unique_together = (('today_id', 'datetime', 'patient_id'),)

class medication_data(models.Model):
    med_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)
    medication1 = models.CharField(max_length=500)
    medication2 = models.CharField(max_length=500)
    medication3 = models.CharField(max_length=500)
    medication4 = models.CharField(max_length=500)
    medication5 = models.CharField(max_length=500)
    syrup1name = models.CharField(max_length=500)
    syrup1quantity = models.CharField(max_length=500)
    syrup2name = models.CharField(max_length=500)
    syrup2quantity = models.CharField(max_length=500)
    syrup3name = models.CharField(max_length=500)
    syrup3quantity = models.CharField(max_length=500)
    datetime = models.DateTimeField()

    class Meta:
        ordering = ['datetime']
        unique_together = (('med_id', 'datetime', 'patient_id'),)

class exercise_data(models.Model):
    exe_id = models.AutoField(primary_key=True)
    walk = models.IntegerField()
    cycling = models.IntegerField()
    pranayam = models.IntegerField()
    stairs = models.IntegerField()
    datetime = models.DateTimeField()
    patient_id = models.ForeignKey(Patient_data, on_delete=models.CASCADE, to_field='patient_id')

    class Meta:
        ordering = ['datetime']
        unique_together = (('exe_id', 'patient_id', 'datetime'),)

class eating_habits_data(models.Model):
    eat_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)
    # breakfast
    bjeerarice = models.CharField(max_length=200, default=None)
    bbiryani = models.CharField(max_length=200, default=None)
    bdal = models.CharField(max_length=200, default=None)
    btikka = models.CharField(max_length=200, default=None)
    bbchicken = models.CharField(max_length=200, default=None)
    bchole = models.CharField(max_length=200, default=None)
    baloogobi = models.CharField(max_length=200, default=None)
    bmixveg = models.CharField(max_length=200, default=None)
    bchickencurry = models.CharField(max_length=200, default=None)

    # lunch
    lbutterchicken = models.CharField(max_length=200, default=None)
    lchole = models.CharField(max_length=200, default=None)
    laloogobi = models.CharField(max_length=200, default=None)
    lupma = models.CharField(max_length=200, default=None)
    lpoha = models.CharField(max_length=200, default=None)
    lidli = models.CharField(max_length=200, default=None)
    ldosa = models.CharField(max_length=200, default=None)
    lalooparatha = models.CharField(max_length=200, default=None)
    lpoori = models.CharField(max_length=200, default=None)
    lbhature = models.CharField(max_length=200, default=None)
    lmeduvada = models.CharField(max_length=200, default=None)
    lsamosa = models.CharField(max_length=200, default=None)

    # dinner
    dtikka = models.CharField(max_length=200, default=None)
    dbutterchecken = models.CharField(max_length=200, default=None)
    dchole = models.CharField(max_length=200, default=None)
    daloogobi = models.CharField(max_length=200, default=None)
    dmixveg = models.CharField(max_length=200, default=None)
    dupma = models.CharField(max_length=200, default=None)
    dpoha = models.CharField(max_length=200, default=None)
    didli = models.CharField(max_length=200, default=None)
    dbhature = models.CharField(max_length=200, default=None)
    dmeduvada = models.CharField(max_length=200, default=None)
    dsamosa = models.CharField(max_length=200, default=None)
    dpoori = models.CharField(max_length=200, default=None)
    ddosa = models.CharField(max_length=200, default=None)

    datetime = models.DateTimeField()
    

    class Meta:
        ordering = ['datetime']
        unique_together = (('patient_id', 'datetime', 'eat_id'))

class eating_habits_other(models.Model):
    other_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    breakfast = models.CharField(max_length=500, default=None, null=True, blank=True)
    lunch = models.CharField(max_length=500, default=None, null=True, blank=True)
    high_tea = models.CharField(max_length=500, default=None, null=True, blank=True)
    dinner = models.CharField(max_length=500, default=None, null=True, blank=True)

    class Meta:
        ordering = ['datetime']
        unique_together = (('patient_id', 'datetime', 'other_id'),)

class prescription_data(models.Model):
    pres_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)
    doctorname = models.CharField(max_length=200, default=None, null=True, blank=True)
    prescription = models.FileField(max_length=200)
    datetime = models.DateTimeField()

    class Meta:
        ordering = ['datetime']
        unique_together = (('patient_id', 'datetime', 'pres_id'),)

class iglu_data(models.Model):
    iglu_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient_data, to_field='patient_id', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    glucoserbs = models.CharField(max_length=50, default=None, null=True, blank=True)

    class Meta:
        ordering = ['datetime']
        unique_together = (('iglu_id', 'patient_id', 'datetime'),)









    

