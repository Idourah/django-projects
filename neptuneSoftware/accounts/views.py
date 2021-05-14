from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView
from accounts.models import Account
from .forms import CustomerSignUpForm, LoginForm
from django.contrib.auth import (
     login, logout, authenticate
)
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_customer:
                return redirect('dashboard')
            else:
                return redirect('manager_home')
        else:
            messages.warning(request, 'incorrect email or password')
    form = LoginForm()
    return render(request, 'auths/login.html', {'form': form})


def logoutPage(request):
    logout(request)
    return redirect('login')


class CustomerSignUpView(CreateView):
    model = Account
    form_class = CustomerSignUpForm
    template_name = 'auths/registration.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('dashboard')
