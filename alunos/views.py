from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acessar_alunos(request):
    return render(request, 'cadastro_aluno.html')


def criar_evento(request):
    return render(request, 'criar_evento.html')