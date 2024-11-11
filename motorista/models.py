from django.db import models

class Motorista(models.Model):
    id = models.AutoField(primary_key=True)
    nome_motorista = models.TextField(max_length=255)
    placa_veiculo = models.TextField(max_length=255)
    pessoa_fisica = models.BooleanField()
    cnh = models.TextField(max_length=255, null=True)