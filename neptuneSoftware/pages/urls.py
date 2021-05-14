from django.urls import path
from pages import views as pages_view

urlpatterns = [
    path('', pages_view.index, name='index'),
    path('home/', pages_view.home, name='home'),
    path('about/', pages_view.about, name='about'),
    path('contact/', pages_view.contact, name='contact'),
    path('portfolio/', pages_view.portfolio, name='portfolio'),
    path('features/', pages_view.features, name='features'),
]