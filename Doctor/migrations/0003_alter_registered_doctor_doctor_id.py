# Generated by Django 4.2.4 on 2023-08-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_registered_doctor_dconfirmpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registered_doctor',
            name='doctor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
