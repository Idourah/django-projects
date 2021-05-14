from django.urls import path
from .views import loginPage, logoutPage, CustomerSignUpView


urlpatterns = [
    path('login',  loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', CustomerSignUpView.as_view(), name='register'),
]
