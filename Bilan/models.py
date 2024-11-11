from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Sum

from Accounts.models import CustomUser

User = get_user_model()


class BilanMensuel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()  # Date du mois de bilan (ex: 2024-11-01)
    total_income = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_fixed(self):
        return self.depenses.filter(category='FIXES').aggregate(Sum('amount'))['amount__sum'] or 0

    @property
    def total_pleasure(self):
        return self.depenses.filter(category='PLAISIR').aggregate(Sum('amount'))['amount__sum'] or 0

    @property
    def total_investments(self):
        return self.depenses.filter(category='INVEST').aggregate(Sum('amount'))['amount__sum'] or 0

    @property
    def total_savings(self):
        return self.depenses.filter(category='EPARGNE').aggregate(Sum('amount'))['amount__sum'] or 0

    @property
    def total_expenses(self):
        return self.total_fixed + self.total_pleasure + self.total_investments + self.total_savings

    @property
    def rav(self):
        return self.total_income - self.total_expenses

    def proportions(self):
        total_expenses = self.total_expenses
        return {
            "fixed": (self.total_fixed / total_expenses * 100) if total_expenses else 0,
            "pleasure": (self.total_pleasure / total_expenses * 100) if total_expenses else 0,
            "investments": (self.total_investments / total_expenses * 100) if total_expenses else 0,
            "savings": (self.total_savings / total_expenses * 100) if total_expenses else 0,
        }
