from django.contrib import admin
from .models import Epargne

@admin.register(Epargne)
class EpargneAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'amount',
        'category',
        'date',
    )
