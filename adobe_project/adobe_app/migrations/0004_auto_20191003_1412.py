# Generated by Django 2.2.5 on 2019-10-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adobe_app', '0003_auto_20191003_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionaldriver',
            name='dl_info',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.DriverLicense'),
        ),
        migrations.AlterField(
            model_name='individualinformation',
            name='cust_driver_license',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.DriverLicense'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='org_representative',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='adobe_app.IndividualInformation'),
        ),
    ]