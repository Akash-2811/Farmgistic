# Generated by Django 3.2 on 2021-04-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_trader_auth_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader_auth',
            name='photo',
            field=models.ImageField(upload_to='media/trader'),
        ),
    ]
