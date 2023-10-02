# Generated by Django 4.2.4 on 2023-09-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0016_patient_data_abha_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='google_client_id',
            field=models.CharField(default='na', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_data',
            name='google_secret_key',
            field=models.CharField(default='na', max_length=1000),
            preserve_default=False,
        ),
    ]
