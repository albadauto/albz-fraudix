from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Motorista
@login_required
def motorista_home(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motorista_home.html', {'motoristas': motoristas})

@login_required
def inserir_motorista(request):
    if request.method == 'POST':
        motorista = Motorista()
        motorista.nome_motorista = request.POST.get('nome')
        motorista.cnh = request.POST.get('cnh')
        motorista.placa_veiculo = request.POST.get('placa')
        motorista.pessoa_fisica = True if request.POST.get('tipo_pessoa') == 'Física' else False
        motorista.save()
        return redirect('motorista_home')
    else:
        return redirect('motorista_home')
    