# Generated by Django 4.0.4 on 2022-05-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_route_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
