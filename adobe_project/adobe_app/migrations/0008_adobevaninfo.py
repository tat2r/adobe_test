# Generated by Django 2.2.5 on 2019-10-03 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adobe_app', '0007_auto_20191003_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdobeVanInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('van_id', models.CharField(max_length=25)),
                ('van_year_make_model', models.CharField(max_length=100)),
                ('van_vin', models.CharField(max_length=25)),
                ('van_plate', models.CharField(max_length=25)),
                ('van_size', models.CharField(max_length=25)),
                ('mileage_start', models.CharField(max_length=25)),
                ('mileage_end', models.CharField(max_length=25)),
                ('van_reg_exp', models.DateField()),
            ],
        ),
    ]