from django.db import models

class Colaborador(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    foto =  models.FileField(upload_to="img",default='')


class Computador (models.Model):
    responsavel = models.OneToOneField(Colaborador,on_delete=models.SET_DEFAULT, default='Sem uso')
    modelo = models.CharField(max_length=255)
    patrimonio = models.CharField(max_length=3)

class Celular (models.Model):
    responsavel = models.OneToOneField(Colaborador,on_delete=models.SET_DEFAULT, default='Sem uso')
    modelo = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    
