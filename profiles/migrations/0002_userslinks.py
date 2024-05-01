# Generated by Django 5.0.3 on 2024-04-16 00:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('user', '0002_remove_customuser_full_name_remove_customuser_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersLinks',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]
