# Generated by Django 4.2.4 on 2023-09-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0009_alter_patient_data_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='image',
            field=models.ImageField(default='', upload_to='patients/image'),
        ),
    ]