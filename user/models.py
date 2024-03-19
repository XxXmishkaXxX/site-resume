from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, user_type, email, number, first_name, second_name,
                    password, sex='M', **extra_fields):
        if not email or not number:
            raise ValueError('Users must have an email address and a phone number')

        email = self.normalize_email(email)
        user = self.model(user_type=user_type, email=email, number=number, first_name=first_name,
                          second_name=second_name, sex=sex, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, number, first_name, second_name, password, **extra_fields):
        user = self.create_user(user_type='ADMIN', email=email, number=number, first_name=first_name,
                                second_name=second_name, password=password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    APPLICANT = 'applicant'
    EMPLOYER = 'employer'
    ADMIN = 'ADMIN'
    USER_TYPE_CHOICES = [
        (APPLICANT, 'Applicant'),
        (EMPLOYER, 'Employer'),
        (ADMIN, 'ADMIN')
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, blank=False)
    email = models.EmailField(unique=True)
    number = PhoneNumberField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    second_name = models.CharField(max_length=30, blank=False)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')), default='M')

    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['number', 'first_name', 'second_name']

    def __str__(self):
        return self.email
