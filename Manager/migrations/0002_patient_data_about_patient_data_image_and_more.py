# Generated by Django 4.2.4 on 2023-09-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='about',
            field=models.CharField(default='nothing', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_data',
            name='image',
            field=models.CharField(default='na', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_data',
            name='phone',
            field=models.IntegerField(default=0, verbose_name=50),
            preserve_default=False,
        ),
    ]