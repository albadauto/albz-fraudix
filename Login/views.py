from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib import messages

def login_home(request):
    logout_user(request)
    return render(request, 'login_home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login_user(request, user)
            return redirect('home:home')
        else:
            messages.error(request, message='Login ou senha incorreto(s)')
            return redirect('login_home')

def logout(request):
    logout_user(request)
    return redirect('login_home')

def create_user(request):
    if request.method == 'GET':
        User.objects.create_user(username="adauto", email="contato@albarraz", password="root")
        return redirect("login_home")