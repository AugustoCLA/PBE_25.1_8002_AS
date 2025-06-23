from django.contrib import admin
from .models import Exercicio

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criado_por')
    search_fields = ('nome',)
