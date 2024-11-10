from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def motorista_home(request):
    return render(request, 'motorista_home.html')