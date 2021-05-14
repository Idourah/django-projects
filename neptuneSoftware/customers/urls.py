from django.urls import path
from customers import views as auth_view

urlpatterns = [

    path('<int:id>/edit_profile', auth_view.CustomerProfile.as_view(), name='customer-profile'),
    path('change_password', auth_view.CustomerChangePasswordView.as_view(), name='change-password'),

]
