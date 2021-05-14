from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from accounts.models import Account
from customers.models import Customer
from django.db import transaction
from django import forms


class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_customer = True
        user.username = '{0} {1}'.format(user.first_name, user.last_name)
        user.save()
        user_group = Group.objects.get(name='Project')
        user.groups.add(user_group)
        Customer.objects.create(user=user)
        return user


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']