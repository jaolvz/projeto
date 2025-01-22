from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    foto =  models.FileField(upload_to="img",default='')


class Computador (models.Model):
    responsavel = models.ForeignKey(Colaborador,on_delete=models.SET_NULL, null=True)
    modelo = models.CharField(max_length=255)
    patrimonio = models.CharField(max_length=3)
    processador = models.CharField(max_length=10)
    quantidade_memoria = models.CharField(max_length=100)

class Celular (models.Model):
    responsavel = models.ForeignKey(Colaborador,on_delete=models.SET_NULL, null=True)
    numero = models.CharField(max_length=10)
    modelo = models.CharField(max_length=255)
    
