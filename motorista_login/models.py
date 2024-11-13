from django.db import models
from motorista.models import Motorista

class MotoristaLoginFront(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.TextField(max_length=20)
    senha = models.TextField(max_length=200)
    telefone = models.TextField(max_length=20)
    motorista = models.OneToOneField(Motorista, on_delete=models.CASCADE)
