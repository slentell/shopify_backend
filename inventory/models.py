from unicodedata import decimal
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator
from django.urls import reverse

# Create your models here.



class Inventory(models.Model):
    name = models.CharField(max_length=100, null = False)
    description = models.CharField(max_length=100, null = False)
    price = MoneyField(decimal_places=2, max_digits=8, default_currency='USD', validators=[MinMoneyValidator(0)] )
    quantity = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)
    deletion_comment = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
        