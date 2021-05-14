from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    ListView,
    DeleteView
)
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth.mixins import PermissionRequiredMixin
from customers.models import Customer
from projects.models import Project
# Create your views here.


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())

        if not self.has_permission():
            return redirect(self.get_login_url())
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class ProjectListView(UserAccessMixin, ListView):
    permission_required = 'projects.view_project'
    raise_exception = False
    login_url = 'login'
    redirect_field_name = 'next'

    model = Project
    template_name = 'projects/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(user=self.request.user)
        context['projects'] = Project.objects.filter(customer=customer)
        return context


class CreateProjectFormView(UserAccessMixin, CreateView):
    permission_required = 'projects.add_project'
    login_url = 'login'
    redirect_field_name = 'next'

    model = Project
    form_class = ProjectForm
    template_name = 'projects/create.html'

    def form_valid(self, form):
        customer = Customer.objects.get(user=self.request.user)
        title = form.cleaned_data.get('title')
        des = form.cleaned_data.get('description')
        budget = form.cleaned_data.get('budget')
        Project.objects.create(customer=customer, title=title, description=des, budget=budget)
        return redirect('dashboard')


class UpdateProjectView(UserAccessMixin, UpdateView):
    permission_required = 'projects.change_project'
    raise_exception = False
    login_url = 'login'
    redirect_field_name = 'next'

    model = Project
    form_class = ProjectForm
    template_name = 'projects/update.html'

    def get_object(self):
        project_id = self.kwargs.get('id')
        return get_object_or_404(Project, id=project_id)


class DetailProjectView(UserAccessMixin, DetailView):
    permission_required = 'projects.view_project'
    raise_exception = False
    login_url = 'login'
    redirect_field_name = 'next'
    model = Project
    template_name = 'projects/details.html'

    def get_object(self):
        project_id = self.kwargs.get('id')
        return get_object_or_404(Project, id=project_id)


def DeleteProjectView(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('dashboard')
    context = {}
    return render(request, 'projects/delete.html', context)

