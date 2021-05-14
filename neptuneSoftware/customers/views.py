from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from accounts.models import Account
from django.urls import reverse_lazy


# Create your views here.
class CustomerProfile(UpdateView):
    model = Account
    fields = ['first_name', 'last_name', 'email']
    template_name = 'users/profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('id')
        return get_object_or_404(Account, id=user_id)

    def form_valid(self, form):
        user = Account.objects.get(id=self.request.user.id)
        username = ''
        lastname = ''
        firstname = ''

        if len(form.cleaned_data.get('first_name')) > 0 and len(form.cleaned_data.get('last_name')):
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            username = '{0} {1}'.format(firstname, lastname)

        if len(form.cleaned_data.get('first_name')) > 0 and len(form.cleaned_data.get('last_name')) == 0:
            firstname = form.cleaned_data.get('first_name')
            username = '{0} {1}'.format(firstname, user.last_name)

        if len(form.cleaned_data.get('first_name')) == 0 and len(form.cleaned_data.get('last_name')) > 0:
            lastname = form.cleaned_data.get('last_name')
            username = '{0} {1}'.format(user.first_name, lastname)

        Account.objects.filter(id=self.request.user.id)\
            .update(username=username, last_name=lastname, first_name=firstname)
        return redirect('dashboard')


class CustomerChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('dashboard')



