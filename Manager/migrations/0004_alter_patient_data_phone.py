# Generated by Django 4.2.4 on 2023-09-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_alter_patient_data_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]