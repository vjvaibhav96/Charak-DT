# Generated by Django 4.2.4 on 2023-10-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0020_patient_data_esio_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='threed',
            field=models.CharField(default=0, max_length=5),
        ),
    ]
