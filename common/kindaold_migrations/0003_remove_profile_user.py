# Generated by Django 2.2.11 on 2020-08-31 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
