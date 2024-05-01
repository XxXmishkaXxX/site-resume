from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        initial = kwargs.get('initial', {})
        if instance:
            initial['full_name'] = instance.full_name
            initial['sex'] = instance.sex
            initial['bio'] = instance.bio
            initial['country'] = instance.country
            initial['city'] = instance.city
            initial['birth_date'] = instance.birth_date
            initial['avatar'] = instance.avatar
        kwargs['initial'] = initial
        super(UserProfileForm, self).__init__(*args, **kwargs)

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']

        if len(full_name) > 300:
            raise ValidationError("ФИО не должно превышать 300 символов.")
        for string in full_name.split():
            if len(string) < 2:
                raise ValidationError("Имя, Фамилия или Отчество должны быть длиннее 1 символа")

        return full_name

    class Meta:
        model = UserProfile
        fields = ['full_name', 'sex', 'bio', 'country', 'city', 'birth_date', 'avatar']
        labels = {
            'full_name': 'Full Name',
            'bio': 'Bio',
            'sex': 'Sex',
            'country': 'Country',
            'city': 'City',
            'birth_date': 'Birth Date',
            'avatar': 'Avatar',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'birth_date': forms.DateInput(format='%d/%m/%Y'),
        }


class EditUserProfileForm():
    pass
