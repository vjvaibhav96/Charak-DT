# Generated by Django 4.2.4 on 2023-08-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pathologist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registered_pathologist',
            name='pconfirmpassword',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registered_pathologist',
            name='ppassword',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
    ]