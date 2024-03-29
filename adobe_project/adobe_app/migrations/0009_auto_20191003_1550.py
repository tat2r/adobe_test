# Generated by Django 2.2.5 on 2019-10-03 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adobe_app', '0008_adobevaninfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='VanRental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_date_start', models.DateTimeField()),
                ('rental_date_end', models.DateTimeField()),
                ('num_of_vans', models.IntegerField()),
                ('rate_charge', models.IntegerField()),
                ('mileage_over_charge', models.IntegerField()),
                ('late_charge', models.IntegerField()),
                ('fuel_charge', models.IntegerField()),
                ('damage_charge', models.IntegerField()),
                ('additional_driver', models.IntegerField()),
                ('under_age', models.IntegerField()),
                ('drop_fee', models.IntegerField()),
                ('mexico_insurance', models.IntegerField()),
                ('cleaning_fee', models.IntegerField()),
                ('other_charges', models.IntegerField()),
                ('surcharge', models.IntegerField()),
                ('license_tax', models.IntegerField()),
                ('sales_tax', models.IntegerField()),
                ('airport_access_fee', models.IntegerField()),
                ('subtotal_out', models.IntegerField()),
                ('total_due', models.IntegerField()),
                ('subtotal_in', models.IntegerField()),
                ('grand_total', models.IntegerField()),
                ('org_name', models.ForeignKey(blank=True, on_delete='CASCADE', to='adobe_app.Organization')),
                ('rentee_name', models.ForeignKey(blank=True, on_delete='CASCADE', to='adobe_app.IndividualInformation')),
            ],
        ),
        migrations.DeleteModel(
            name='RentalEvent',
        ),
        migrations.AlterField(
            model_name='adobevaninfo',
            name='mileage_end',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='adobevaninfo',
            name='mileage_start',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
