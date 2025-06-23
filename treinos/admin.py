from django.contrib import admin
from .models import Treino, TreinoExercicio

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'usuario', 'data_criacao')
    search_fields = ('nome',)

@admin.register(TreinoExercicio)
class TreinoExercicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'treino', 'exercicio', 'ordem', 'repeticoes')  


