from django.shortcuts import render,get_object_or_404, redirect
from .models import Colaborador, Celular, Computador
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib. auth import authenticate, login
import os



@login_required(login_url='home:login')
def pagina_inicial(request):
    return render(request,'index.html')
@login_required(login_url='home:login')
def celulares(request):
    colaboradores = Colaborador.objects.filter(celulares=None)
    celulares = Celular.objects.all()
    contexto = {'colaboradores':colaboradores,'celulares': celulares}
    return render(request,'celulares.html', contexto)

@login_required(login_url='home:login')
def computadores(request):
    colaboradores = Colaborador.objects.filter(computadores=None)
    estoque = Colaborador.objects.filter(nome='Estoque')
    colaboradores = colaboradores | estoque
    computadores = Computador.objects.all()
    contexto = {'colaboradores':colaboradores,'computadores': computadores}
    return render(request,'computadores.html', contexto)
@login_required(login_url='home:login')
def colaboradores(request):
    Colaboradores = Colaborador.objects.all()  
    return render(request,'colaboradores.html', {'colaboradores': Colaboradores})
      
@csrf_exempt
def cadastro (request):
    if   request.method == 'GET':
        if request.user.is_authenticated:
            return  redirect('home:pagina_inicial')
        else:
            return render (request, 'login.html')
    else:
        username_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = User.objects.create_user(username=username_usuario, password=senha)
        usuario.save()
        return redirect ('home:login')

@csrf_exempt    
def logar(request):
    if   request.method == 'GET':
        if request.user.is_authenticated:
            return  render (request, 'index.html')
        else:
            return render (request, 'login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=username, password=senha)
        if usuario:
            login(request,usuario)
            return redirect('home:pagina_inicial')
        else:
            return render(request,'login.html') # usuario nao existe
        
@login_required(login_url='home:login')       
def perfil  (request, id):
    colaborador  = get_object_or_404(Colaborador, id=id)
    return render (request, 'perfil.html', {'colaborador':colaborador})


@login_required(login_url='home:login')
def excluir_colaborador(request,id):
    colaborador = get_object_or_404(Colaborador, id=id)
    colaborador.delete()
    return redirect('home:colaboradores')
@login_required(login_url='home:login')
def excluir_computador(request,id):
    computador = get_object_or_404(Computador, id=id)
    computador.delete()
    return redirect('home:computadores')
@login_required(login_url='home:login')
def excluir_celular(request,id):
    celular = get_object_or_404(Celular, id=id)
    celular.delete()
    return redirect('home:celulares')



@login_required(login_url='home:login')
def adicionar_computador(request):
    if request.method == 'POST':
        responsavel_id = request.POST.get('responsavel')
        modelo = request.POST.get('modelo')
        patrimonio = request.POST.get('patrimonio')
        processador = request.POST.get('processador')
        memoria = request.POST.get('qtd_memoria')
        responsavel =get_object_or_404(Colaborador, id= responsavel_id)
        celular = Computador.objects.create(responsavel=responsavel, patrimonio=patrimonio,modelo=modelo, processador= processador, quantidade_memoria = memoria)
        return redirect('home:computadores')
    else:
        return render(request,'home.html')
@login_required(login_url='home:login')
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
@login_required(login_url='home:login')  
def adicionar_celular (request):#feito
    if request.method == 'POST':
        responsavel_id = request.POST.get('responsavel')
        modelo_celular = request.POST.get('modelo')
        numero = request.POST.get('numero')
        responsavel =get_object_or_404(Colaborador, id= responsavel_id)
        celular = Celular.objects.create(responsavel=responsavel, modelo=modelo_celular,numero=numero)
        return redirect('home:celulares')
    else:
        return render(request,'home.html')