# Generated by Django 4.2.4 on 2023-09-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0018_patient_data_report_patient_data_xray'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='abha_id',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='about',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='age',
            field=models.IntegerField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='bloodpressure',
            field=models.IntegerField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='bmi',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='brushinghabits',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='chestpaintype',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='cholestrol',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='dailyexercise',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='dpf',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='fulladdress',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='fullname',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='gender',
            field=models.IntegerField(blank=True, default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='glucosevalue',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='google_client_id',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='google_secret_key',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='patients/images'),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='insulinvalue',
            field=models.IntegerField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='otp',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='prediabetic',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='prescription',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='report',
            field=models.FileField(blank=True, default=None, null=True, upload_to='patients/reports'),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='sleepinghabits',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='xray',
            field=models.FileField(blank=True, default=None, null=True, upload_to='patients/xray'),
        ),
    ]