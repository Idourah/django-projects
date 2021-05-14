from django.db import models
from accounts.models import Account
# Create your models here.


class Manager(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    project_counter = models.IntegerField()
