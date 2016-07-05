from django.contrib import admin
from .models import Aluno, Professor


class AlunoAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'email')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor)
