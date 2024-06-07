from django.shortcuts import render, redirect
from .models import Car, Request
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm


# Create your views here.
def index(request):
    all_cars = Car.objects.all()
    return render(request, 'main/index.html', {'all_cars': all_cars})


def checkout(request, car_id):
    if request.method == 'POST':
        return render(request, 'main/success.html')
    else:
        return render(request, 'main/checkout.html', {'car_id': car_id})


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})


# login.css page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('main:index')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('main:login')


def details(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'main/details.html', {'car': car})


def low_high(request):
    all_cars = Car.objects.order_by('car_price')
    return render(request, 'main/index.html', {'all_cars': all_cars})


def high_low(request):
    all_cars = Car.objects.order_by('-car_price')
    return render(request, 'main/index.html', {'all_cars': all_cars})
