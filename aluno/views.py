from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Aluno


class DetailAlunoView(DetailView):
    template_name= 'alunos/index.html'
    model = Aluno


class ListaAlunosView(ListView):
    template_name = 'alunos/index.html'
    model = Aluno


def teste_view(request):
    return HttpResponse('As piadas do Luiz sao otimas')


def minha_url(request, idade):
    return HttpResponse(idade)


def url(request):
    aluno = get_object_or_404(Aluno, pk=10)
    context = {'aluno': aluno }
    return render(request, 'alunos/index.html', context)
