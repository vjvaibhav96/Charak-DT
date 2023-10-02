# Generated by Django 4.2.4 on 2023-09-29 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_alter_eating_habits_data_baloogobi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_condition_data',
            name='arthritis',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='asthama',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='cancer',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='diabetes',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='gastrointestinal_disorder',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='hearing_loss',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='heart_disease',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='hiv_aids',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='mental_health',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='obesity',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='post_traumatic_stress_disorder',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='health_condition_data',
            name='stroke',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
