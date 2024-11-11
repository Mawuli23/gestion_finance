from django import forms
from .models import Revenu

class RevenuForm(forms.ModelForm):
    class Meta:
        model = Revenu
        fields = ['category', 'name', 'amount']

"""
class CategorieRevenuForm(forms.ModelForm):
    class Meta:
        model = CategorieRevenu
        fields = ['name']"""
