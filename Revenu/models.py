from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from Accounts.models import CustomUser

User = get_user_model()

"""

class CategorieRevenu(models.Model):
    TYPE_CHOICES = [
        ('Fixes', 'Fixe'),
        ('Variables', 'Variable'),
    ]

    name = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
"""

class Revenu(models.Model):
    TYPE_CHOICES = [
        ('Fixes', 'Fixe'),
        ('Variables', 'Variable'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.category} - {self.amount} €"

