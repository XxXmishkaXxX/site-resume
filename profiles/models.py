import os

from cities_light.models import Country, City
from django.db import models

from django.contrib.auth import get_user_model

CustomUser = get_user_model()


def user_file_path(instance, filename, folder):
    return os.path.join(folder, instance.user.email, filename)


class UserProfile(models.Model):

    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=254, blank=False)
    bio = models.TextField(max_length=1000, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=False)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default_avatar.png')

    def __str__(self):
        return f'Profile of {self.user}'


class UsersLinks(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    link = models.CharField(max_length=1000, blank=False)
