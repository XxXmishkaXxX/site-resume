from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


class CustomSignupForm(SignupForm):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    full_name = forms.CharField(max_length=254, label='ФИО')
    sex = forms.ChoiceField(choices=SEX_CHOICES, label='Пол')

    def clean_email(self):
        email = self.cleaned_data['email']
        allowed_domains = ['gmail.com', 'mail.ru', 'yandex.ru']
        domain = email.split('@')[-1]
        if domain not in allowed_domains:
            raise ValidationError("Недопустимый почтовый домен.")

        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Этот адрес электронной почты уже зарегистрирован.")

        return email

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']

        if len(full_name) > 200:
            raise ValidationError("ФИО не должно превышать 200 символов.")
        if full_name.count(' ') > 2:
            raise ValidationError("ФИО должно содержать не более двух пробелов.")
        for string in full_name.split():
            if len(string) < 2:
                raise ValidationError("Имя, Фамилия или Отчество должны быть длиннее 1 символа")

        return full_name

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.sex = self.cleaned_data['sex']
        user.save()
        return user
