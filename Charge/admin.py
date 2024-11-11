from django.contrib import admin
from .models import Charge

"""
# Register your models here.
@admin.register(CategorieCharge)
class CategorieChargeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
"""

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'category',
        'amount',
    )