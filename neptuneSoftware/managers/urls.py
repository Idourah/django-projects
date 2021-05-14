from django.urls import path
from managers import views as manager_view


urlpatterns = [
    path('home', manager_view.ManagerDashboardView.as_view(), name='manager_home'),
    path('desktop', manager_view.ManagerProjectView.as_view(), name='manager_desktop'),
    path('customers', manager_view.ManagerCustomersView.as_view(), name='manager_customer'),
    path('messages',manager_view.ManagerMessageView.as_view(), name='manager_message')
]