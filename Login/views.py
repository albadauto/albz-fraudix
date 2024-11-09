from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user

def login_home(request):
    return render(request, 'login_home.html')


def login(request):
    if request.method == 'POST':
        user = authenticate(username="adauto", password="root")
        if user:
            login_user(request, user)
            return redirect('home:home')
        else:
            print('usuário ou senha incorreto(s)')

def logout(request):
    return redirect('home:home')

def create_user(request):
    if request.method == 'GET':
        User.objects.create_user(username="adauto", email="contato@albarraz", password="root")
        return redirect("login_home")