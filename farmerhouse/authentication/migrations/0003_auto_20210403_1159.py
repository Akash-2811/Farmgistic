# Generated by Django 3.1.7 on 2021-04-03 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210331_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_auth',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trader_auth',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
