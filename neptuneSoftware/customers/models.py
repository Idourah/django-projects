from django.db import models
from accounts.models import Account

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
