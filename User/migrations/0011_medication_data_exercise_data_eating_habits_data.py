# Generated by Django 4.2.4 on 2023-09-29 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0018_patient_data_report_patient_data_xray'),
        ('User', '0010_vitals_data_todays_feel_data_health_condition_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='medication_data',
            fields=[
                ('med_id', models.AutoField(primary_key=True, serialize=False)),
                ('medication1', models.CharField(max_length=500)),
                ('medication2', models.CharField(max_length=500)),
                ('medication3', models.CharField(max_length=500)),
                ('medication4', models.CharField(max_length=500)),
                ('medication5', models.CharField(max_length=500)),
                ('syrup1name', models.CharField(max_length=500)),
                ('syrup1quantity', models.CharField(max_length=500)),
                ('syrup2name', models.CharField(max_length=500)),
                ('syrup2quantity', models.CharField(max_length=500)),
                ('syrup3name', models.CharField(max_length=500)),
                ('syrup3quantity', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.patient_data')),
            ],
            options={
                'ordering': ['datetime'],
                'unique_together': {('med_id', 'datetime', 'patient_id')},
            },
        ),
        migrations.CreateModel(
            name='exercise_data',
            fields=[
                ('exe_id', models.AutoField(primary_key=True, serialize=False)),
                ('walk', models.IntegerField()),
                ('cycling', models.IntegerField()),
                ('pranayam', models.IntegerField()),
                ('stairs', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.patient_data')),
            ],
            options={
                'ordering': ['datetime'],
                'unique_together': {('exe_id', 'patient_id', 'datetime')},
            },
        ),
        migrations.CreateModel(
            name='eating_habits_data',
            fields=[
                ('eat_id', models.AutoField(primary_key=True, serialize=False)),
                ('bjeerarice', models.CharField(max_length=200)),
                ('bbiryani', models.CharField(max_length=200)),
                ('bdal', models.CharField(max_length=200)),
                ('btikka', models.CharField(max_length=200)),
                ('bbchicken', models.CharField(max_length=200)),
                ('bchole', models.CharField(max_length=200)),
                ('baloogobi', models.CharField(max_length=200)),
                ('bmixveg', models.CharField(max_length=200)),
                ('bchickencurry', models.CharField(max_length=200)),
                ('lbutterchicken', models.CharField(max_length=200)),
                ('lchole', models.CharField(max_length=200)),
                ('laloogobi', models.CharField(max_length=200)),
                ('lupma', models.CharField(max_length=200)),
                ('lpoha', models.CharField(max_length=200)),
                ('lidli', models.CharField(max_length=200)),
                ('ldosa', models.CharField(max_length=200)),
                ('lalooparatha', models.CharField(max_length=200)),
                ('lpoori', models.CharField(max_length=200)),
                ('lbhature', models.CharField(max_length=200)),
                ('lmeduvada', models.CharField(max_length=200)),
                ('lsamosa', models.CharField(max_length=200)),
                ('dtikka', models.CharField(max_length=200)),
                ('dbutterchecken', models.CharField(max_length=200)),
                ('dchole', models.CharField(max_length=200)),
                ('daloogobi', models.CharField(max_length=200)),
                ('dmixveg', models.CharField(max_length=200)),
                ('dupma', models.CharField(max_length=200)),
                ('dpoha', models.CharField(max_length=200)),
                ('didli', models.CharField(max_length=200)),
                ('dbhature', models.CharField(max_length=200)),
                ('dmeduvada', models.CharField(max_length=200)),
                ('dsamosa', models.CharField(max_length=200)),
                ('dpoori', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Manager.patient_data')),
            ],
            options={
                'ordering': ['datetime'],
                'unique_together': {('patient_id', 'datetime', 'eat_id')},
            },
        ),
    ]
