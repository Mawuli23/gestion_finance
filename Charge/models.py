from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from Accounts.models import CustomUser

User = get_user_model()

"""
class CategorieCharge(models.Model):
    TYPE_CHOICES = [
        ('Fixes', 'Fixe'),
        ('Variables', 'Variable'),
    ]

    name = models.CharField(max_length=10, choices=TYPE_CHOICES)
    #type_categorie = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name}"
"""

class Charge(models.Model):
    TYPE_CHOICES = [
        ('Fixes', 'Fixe'),
        ('Variables', 'Variable'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.amount} €"

