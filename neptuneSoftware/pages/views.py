from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'pages/home.html', {})


def about(request):
    return render(request, 'pages/about.html', {})


def contact(request):
    return render(request, 'pages/contact.html', {})


def features(request):
    return render(request, 'pages/features.html', {})


def portfolio(request):
    return render(request, 'pages/portfolio.html', {})
