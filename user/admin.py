from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'full_name', 'sex', 'is_active', 'date_joined',)
    ordering = ('is_staff',)


admin.site.register(CustomUser, CustomUserAdmin)
