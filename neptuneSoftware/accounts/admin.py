from django.contrib import admin
from customers.models import Customer
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerSignUpForm
from .models import Account
from django.contrib.auth.forms import UserCreationForm


# Register your models here.

class AccountCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'password1', 'password2']


class AccountAdmin(UserAdmin):
    model = Account
    add_form = AccountCreationForm
    fieldsets = (*UserAdmin.fieldsets, ('User role', {'fields': ('is_admin', 'is_manager', 'is_customer')}))


admin.site.register(Account, AccountAdmin)

