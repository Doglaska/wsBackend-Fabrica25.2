from django.shortcuts import render, redirect
from .models import Aluno, Professor
from .forms import AlunoForm, ProfessorForm
import requests
from django.http import HttpResponse

#Home geral
def home(request):
    return render(request, 'app/home.html')

#CRUD dos alunos
def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'app/listar.html', {'alunos': alunos})

def criarAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarAlunos')
    else:
        form = AlunoForm()
    return render(request, 'app/criar.html', {'aluno': form})

def deletarAluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listarAlunos')
    return render(request, 'app/deletar.html', {'aluno': aluno})

def atualizarAluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance = aluno)
        if form.is_valid():
            form.save()
            return redirect('listarAlunos')
    else:
        form = AlunoForm(instance = aluno)
    return render(request, 'app/criar.html', {'aluno': form})


#CRUD dos professores
def listarProfessores(request):
    professores = Professor.objects.all()
    return render(request, 'app/listarP.html', {'professores': professores})

def criarProfessor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProfessores')
    else:
        form = ProfessorForm()
    return render(request, 'app/criarP.html', {'professor': form})

def deletarProfessor(request, pk):
    professor = Professor.objects.get(pk=pk)
    if request.method == 'POST':
        professor.delete()
        return redirect('listarProfessores')
    return render(request, 'app/deletarP.html', {'professor': professor})

def atualizarProfessor(request, pk):
    professor = Professor.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance = professor)
        if form.is_valid():
            form.save()
            return redirect('listarProfessores')
    else:
        form = ProfessorForm(instance = professor)
    return render(request, 'app/criarP.html', {'professor': form})

#API de localizacao
def localizarIp(request):
    response = requests.get("http://ip-api.com/json/")
    dados = response.json()
    if dados.get('status') == 'success':
        conteudo = f"""
        <h1>Localização do IP</h1>
        <p><strong>IP:</strong> {dados.get('query')}</p>
        <p><strong>País:</strong> {dados.get('country')}</p>
        <p><strong>Região:</strong> {dados.get('regionName')}</p>
        <p><strong>Cidade:</strong> {dados.get('city')}</p>
        """
    else:
        conteudo = "<p>Não foi possível obter os dados de localização.</p>"

    return HttpResponse(conteudo)
