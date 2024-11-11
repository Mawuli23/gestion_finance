from django.contrib import admin

# Register your models here.

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'prenom_1',
        'prenom_2',
        'email',
        'is_active',
        'is_staff',
        'is_admin',
    )
    list_editable = (
        'is_staff',
        'is_admin',
    )
