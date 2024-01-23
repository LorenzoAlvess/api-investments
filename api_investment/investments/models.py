# investments/models.py

from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=50)
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    return_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    term = models.IntegerField(null=True, blank=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, default='active')
    location = models.CharField(max_length=100, null=True, blank=True)
    issuer_entity = models.CharField(max_length=100, null=True, blank=True)
    market_data = models.CharField(max_length=100, null=True, blank=True)
    strategy = models.TextField(null=True, blank=True)

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investments = models.ManyToManyField(Investment, related_name='account_investments')

    def update_balance(self):
        # Calcula o saldo somando os valores dos investimentos associados
        total_investment_value = self.investments.aggregate(models.Sum('value'))['value__sum'] or 0
        self.balance = total_investment_value
        self.save()

    def save(self, *args, **kwargs):
        # Atualiza automaticamente o saldo ao salvar
        self.update_balance()
        super(Account, self).save(*args, **kwargs)
