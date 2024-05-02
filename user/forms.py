from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomSignupForm(SignupForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domains = ['gmail.com', 'mail.ru', 'yandex.ru']
        domain = email.split('@')[-1]
        if domain not in allowed_domains:
            self.add_error('email', "Недопустимый почтовый домен.")
            raise ValidationError("Недопустимый почтовый домен.")

        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', "Этот адрес электронной почты уже зарегистрирован.")
            raise ValidationError("Этот адрес электронной почты уже зарегистрирован.")

        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.save()
        return user
