# Generated by Django 4.2.4 on 2023-08-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_doctor',
            name='dconfirmpassword',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registered_doctor',
            name='dpassword',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
