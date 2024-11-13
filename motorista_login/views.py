from django.shortcuts import render, redirect
from motorista.models import Motorista
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import MotoristaLoginFront
import bcrypt
import json

@login_required
def motorista_login_home(request):
    motoristas_login = MotoristaLoginFront.objects.select_related('motorista')
    motorista = Motorista.objects.all()
    return render(request, 'motorista_login_home.html', {"motoristas_login": motoristas_login, "motoristas": motorista })

def inserir_alterar_motorista_login(request):
    try:
        if request.method == 'POST':
            motoristaloginfront = MotoristaLoginFront()
            id = request.POST.get('id')
            motorista = Motorista.objects.get(id=request.POST.get('motorista'))
            login_existente = MotoristaLoginFront.objects.filter(motorista=motorista).first()
            motoristaloginfront.usuario = request.POST.get('usuario')
            motoristaloginfront.senha = criptografar_senha(request.POST.get('senha'))
            motoristaloginfront.telefone = request.POST.get('telefone')
            motoristaloginfront.motorista = motorista
            if login_existente is not None:
                messages.error(request, message="Já existe um usuário com este motorista.")
                return redirect('motorista_login_home')
            if id is not None and id != '':
                alterar_motorista(usuario=motoristaloginfront.usuario, senha=motoristaloginfront.senha, telefone=motoristaloginfront.telefone, motorista=motorista, id=id)
                messages.success(request, message="Alterado com sucesso!")
                return redirect('motorista_login_home')
            else:
                motoristaloginfront.save()
                messages.success(request, message="Inserido com sucesso!")
                return redirect('motorista_login_home')
               
    except Exception as e:
        messages.error(request, message="Ocorreu um erro interno. Favor, enviar um report para contato@albarraz.com.br. Mensagem original: " + str(e))
        return redirect('motorista_login_home')
    

def excluir_motorista_login(request, id):
    try:
        if request.method == 'GET':
            motorista_login_para_excluir = MotoristaLoginFront.objects.get(id=id)
            motorista_login_para_excluir.delete()
            messages.success(request, message="Excluído com sucesso!")
            return redirect('motorista_login_home')
    except Exception as e:
         messages.error(request, message="Ocorreu um erro interno. Favor, enviar um report para contato@albarraz.com.br. Mensagem original: " + str(e))
         return redirect('motorista_login_home')

def criptografar_senha(senha):
     salt = bcrypt.gensalt()
     senha_hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
     return senha_hashed

def buscar_motorista_login(request, id):
    try:
        if request.method == 'GET':
            motorista_login = MotoristaLoginFront.objects.select_related('motorista').get(id=id)
            data = {
                "id": motorista_login.id,
                "usuario": motorista_login.usuario,
                "motorista": motorista_login.motorista.id,
                "telefone": motorista_login.telefone
            }
            if motorista_login is not None:
                return JsonResponse({"data": data, "success": True })
    except Exception as e:
        print(e.args)

def alterar_motorista(id, usuario, senha, telefone, motorista):
    try:
        MotoristaLoginFront.objects.filter(id=id).update(usuario=usuario, senha=senha, telefone=telefone, motorista=motorista)
    except Exception as e:
        print(e.args)