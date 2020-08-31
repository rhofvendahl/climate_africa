# Generated by Django 2.2.11 on 2020-08-31 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0008_city_timezone'),
        ('common', '0003_auto_20200831_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='default_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cities_light.City'),
        ),
    ]
