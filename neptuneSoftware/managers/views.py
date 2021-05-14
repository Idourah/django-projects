from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Manager
from accounts.models import Account
from projects.models import Project
from customers.models import Customer

# Create your views here


class ManagerDashboardView(TemplateView):
    model = Manager
    template_name = 'managers/manager_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()[:3]
        context['customers'] = Account.objects.filter(is_customer=True)[:4]
        context['CountProject'] = Project.objects.count()
        context['DoneProject'] = Project.objects.filter(status=True).count()
        context['PendingProject'] = Project.objects.filter(status=False).count()
        context['CountCustomer'] = Account.objects.filter(is_customer=True).count()
        return context


class ManagerProjectView(TemplateView):
    model = Manager
    template_name = 'managers/manager_desktop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class ManagerCustomersView(TemplateView):
    model = Manager
    template_name = 'managers/manager_customers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customers'] = Account.objects.filter(is_customer=True)
        return context


class ManagerMessageView(TemplateView):
    model = Manager
    template_name = 'managers/manager_message.html'

