from django.shortcuts import render,get_object_or_404, redirect, HttpResponse
from .models import Colaborador, Celular, Computador
from django.contrib import messages
import os




def index(request):
    return render(request,'index.html')
def celulares(request):
    colaboradores = Colaborador.objects.filter(celular=None)
    celulares = Celular.objects.all()
    contexto = {'colaboradores':colaboradores,'celulares': celulares}
    return render(request,'celulares.html', contexto)

def computadores(request):
    colaboradores = Colaborador.objects.filter(computador=None)
    computadores = Computador.objects.all()
    contexto = {'colaboradores':colaboradores,'computadores': computadores}
    return render(request,'computadores.html', contexto)

def colaboradores(request):
    Colaboradores = Colaborador.objects.all()  
    return render(request,'colaboradores.html', {'colaboradores': Colaboradores})
      

def perfil  (request, id):
    colaborador  = get_object_or_404(Colaborador, id=id);
    return render (request, 'perfil.html', {'colaborador':colaborador})



def excluir_colaborador(request,id):
    colaborador = get_object_or_404(Colaborador, id=id)
    nome = colaborador.nome
    colaborador.delete()
    return redirect('home:colaboradores')


def adicionar_computador(request):
    if request.method == 'POST':
        responsavel_id = request.POST.get('responsavel')
        modelo = request.POST.get('modelo')
        patrimonio = request.POST.get('patrimonio')
        responsavel =get_object_or_404(Colaborador, id= responsavel_id)
        celular = Computador.objects.create(responsavel=responsavel, patrimonio=patrimonio,modelo=modelo)
        return redirect('home:computadores')
    else:
        return render(request,'home.html')

def adicionar_colaborador(request): #feito
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')

        email_existe = Colaborador.objects.filter(email=email).first()
        if email_existe:
            erro ='Email já cadastrado!'
            return render(request,'colaboradores.html',{'erro':erro}) 
        colaborador= Colaborador.objects.create(nome=nome, email=email)
        return redirect('home:colaboradores') 
    else:
        return render(request,'home.html')
    
def adicionar_celular (request):#feito
    if request.method == 'POST':
        responsavel_id = request.POST.get('responsavel')
        modelo = request.POST.get('modelo')
        numero = request.POST.get('numero')
        responsavel =get_object_or_404(Colaborador, id= responsavel_id)
        celular = Celular.objects.create(responsavel=responsavel, modelo=modelo,numero=numero)
        return redirect('home:celulares')
    else:
        return render(request,'home.html')