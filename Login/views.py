from django.shortcuts import render, redirect

def login_home(request):
    return render(request, 'login_home.html')


def login(request):
    if request.method == 'POST':
        print('foi')
        return redirect('home:home')