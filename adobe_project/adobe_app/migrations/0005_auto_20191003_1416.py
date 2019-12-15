# Generated by Django 2.2.5 on 2019-10-03 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adobe_app', '0004_auto_20191003_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arrivingflight',
            old_name='arriving_date',
            new_name='arriving_date_time',
        ),
        migrations.RenameField(
            model_name='departingflight',
            old_name='departing_date',
            new_name='departing_date_time',
        ),
        migrations.RemoveField(
            model_name='arrivingflight',
            name='arriving_time',
        ),
        migrations.RemoveField(
            model_name='departingflight',
            name='departing_time',
        ),
        migrations.AlterField(
            model_name='arrivingflight',
            name='arriving_airline',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='arrivingflight',
            name='arriving_airport',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='arrivingflight',
            name='arriving_flight_number',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cc_exp',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='departingflight',
            name='departing_airline',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='departingflight',
            name='departing_airport',
            field=models.CharField(max_length=125),
        ),
        migrations.AlterField(
            model_name='departingflight',
            name='departing_flight_number',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='driverlicense',
            name='dl_dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='driverlicense',
            name='dl_exp',
            field=models.DateField(),
        ),
    ]
