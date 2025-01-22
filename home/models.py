from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()

class Computador (models.Model):
    responsavel = models.ForeignKey(Colaborador,on_delete=models.SET_NULL, null=True ,related_name="computadores")
    modelo = models.CharField(max_length=255)
    patrimonio = models.CharField(max_length=3)
    processador = models.CharField(max_length=10)
    quantidade_memoria = models.CharField(max_length=100)

class Celular (models.Model):
    responsavel = models.ForeignKey(Colaborador,on_delete=models.SET_NULL, null=True,related_name="celulares")
    numero = models.CharField(max_length=10)
    modelo = models.CharField(max_length=255)
    
