# Generated by Django 4.2.4 on 2023-09-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0019_alter_patient_data_abha_id_alter_patient_data_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='esio_first_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_data',
            name='esio_folder_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient_data',
            name='esio_patient_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
