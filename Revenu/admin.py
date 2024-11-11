from django.contrib import admin
from .models import  Revenu

# Register your models here.

"""
@admin.register(CategorieRevenu)
class CategorieRevenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )"""


@admin.register(Revenu)
class RevenuAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'category',
        'amount',
        'date',
    )
