# Generated by Django 5.0.3 on 2024-04-21 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_userprofile_city_userprofile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]
