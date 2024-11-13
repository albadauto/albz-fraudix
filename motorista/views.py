from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Motorista
from django.contrib import messages

@login_required
def motorista_home(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motorista_home.html', {'motoristas': motoristas})

@login_required
def inserir_motorista(request):
    try:
        if request.method == 'POST':
            motorista = Motorista()
            motorista.nome_motorista = request.POST.get('nome')
            motorista.cnh = request.POST.get('cnh')
            motorista.placa_veiculo = request.POST.get('placa')
            motorista.pessoa_fisica = True if request.POST.get('tipo_pessoa') == 'Física' else False
            if not motorista.nome_motorista or not motorista.cnh or not motorista.placa_veiculo or not motorista.pessoa_fisica:
                messages.error(request, message="Favor, preencher todos os campos corretamente")
            else:
                motorista.save()
            return redirect('motorista_home')
        else:
            return redirect('motorista_home')
    except Exception as e:
        messages.error(request, message="Ocorreu um erro interno. Favor, enviar um report para contato@albarraz.com.br. Mensagem original: " + str(e))
        return redirect('motorista_login_home')
   
    

@login_required
def deletar_motorista(request, id):
    if request.method == 'GET':
        deletar = Motorista.objects.get(id=id)
        if deletar is not None:
            deletar.delete()
            messages.success(request, message='Deletado com sucesso!')
    return redirect('motorista_home')
