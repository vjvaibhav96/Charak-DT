# Generated by Django 4.2.4 on 2023-09-29 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_alter_health_condition_data_arthritis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_condition_data',
            name='diabetes',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]