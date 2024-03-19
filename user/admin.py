from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'number', 'first_name', 'second_name', 'user_type', 'is_active', 'date_joined')
    list_filter = ('user_type', 'is_active')
    search_fields = ('email', 'first_name', 'second_name', 'number')
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('number', 'first_name', 'second_name', 'patronymic', 'sex')}),
        ('Permissions', {'fields': ('user_type', 'is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'number', 'first_name', 'second_name', 'patronymic', 'sex', 'password1', 'password2', 'user_type', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )


# Зарегистрируйте вашу пользовательскую модель и связанный с ней администратор
admin.site.register(CustomUser, CustomUserAdmin)
