from django.db import models
from usuarios.models import Usuario
from exercicios.models import Exercicio


class Treino(models.Model):
    nome = models.CharField("Nome do Treino", max_length=200)
    descricao = models.TextField("Descrição", blank=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name='treinos'
    )
    exercicios = models.ManyToManyField(
        Exercicio,
        through='TreinoExercicio',
        related_name='treinos'
    )
    data_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)
    ativo = models.BooleanField("Ativo", default=True)

    def __str__(self):
        return f"{self.nome} - {self.usuario.get_full_name()}"

    class Meta:
        db_table = 'treinos'
        verbose_name = 'Treino'
        verbose_name_plural = 'Treinos'


class TreinoExercicio(models.Model):
    treino = models.ForeignKey(Treino, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField("Ordem no Treino")
    repeticoes = models.PositiveIntegerField("Repetições", null=True, blank=True)
    duracao_segundos = models.PositiveIntegerField("Duração (segundos)", null=True, blank=True)

    def __str__(self):
        return f"{self.treino.nome} - {self.exercicio.nome} (ordem {self.ordem})"

    class Meta:
        db_table = 'treino_exercicios'
        verbose_name = 'Exercício do Treino'
        verbose_name_plural = 'Exercícios do Treino'
        ordering = ['ordem']

