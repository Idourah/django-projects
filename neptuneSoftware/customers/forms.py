from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class UserChangeDataForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email']
