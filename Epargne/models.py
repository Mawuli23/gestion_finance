from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from Accounts.models import CustomUser

User = get_user_model()

class Epargne(models.Model):
    TYPE_CHOICES = [
        ('Mensuels', 'Mensuel'),
        ('Investissements', 'Investissement'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"
