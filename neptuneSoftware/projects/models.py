from django.db import models
from customers.models import Customer
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    budget = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_date = models.DateField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('detail-project', kwargs={'id': self.id})



