from django.db import models


class Professor(models.Model):
    nome = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{}'.format(self.nome)


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    idade = models.DateField()
    professor = models.ForeignKey(Professor, related_name='alunos')

    def __str__(self):
        return '{}'.format(self.nome)
