from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Exercicio(models.Model):
    nome = models.CharField("Nome do Exercício", max_length=200, unique=True)
    descricao = models.TextField("Descrição")

    GRUPO_MUSCULAR_CHOICES = [
        ('peito', 'Peitoral'),
        ('costas', 'Costas'),
        ('ombros', 'Ombros'),
        ('biceps', 'Bíceps'),
        ('triceps', 'Tríceps'),
        ('quadriceps', 'Quadríceps'),
        ('posterior_coxa', 'Posterior de Coxa'),
        ('gluteos', 'Glúteos'),
        ('panturrilha', 'Panturrilha'),
        ('core', 'Core/Abdômen'),
        ('cardio', 'Cardiovascular'),
    ]
    grupo_muscular_principal = models.CharField(
        "Grupo Muscular Principal",
        max_length=50,
        choices=GRUPO_MUSCULAR_CHOICES
    )

    EQUIPAMENTO_CHOICES = [
        ('peso_corporal', 'Peso Corporal'),
        ('halteres', 'Halteres'),
        ('barra', 'Barra'),
        ('maquina', 'Máquina'),
        ('cabo', 'Cabo/Polia'),
        ('kettlebell', 'Kettlebell'),
        ('elastico', 'Elástico'),
        ('medicine_ball', 'Medicine Ball'),
        ('outros', 'Outros'),
    ]
    equipamento_necessario = models.CharField(
        "Equipamento Necessário",
        max_length=50,
        choices=EQUIPAMENTO_CHOICES,
        default='peso_corporal'
    )

    NIVEL_CHOICES = [
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
    ]
    nivel_dificuldade = models.CharField(
        "Nível de Dificuldade",
        max_length=20,
        choices=NIVEL_CHOICES,
        default='iniciante'
    )

    instrucoes_execucao = models.TextField("Instruções de Execução")

    calorias_por_minuto = models.FloatField(
        "Calorias por Minuto",
        default=5.0,
        validators=[MinValueValidator(0.1), MaxValueValidator(50.0)]
    )

    tempo_execucao_medio = models.PositiveIntegerField(
        "Tempo Médio de Execução (segundos)",
        default=60
    )

    publico = models.BooleanField("Público", default=True)

    criado_por = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
        related_name='exercicios_criados'
    )

    data_criacao = models.DateTimeField("Data de Criação", auto_now_add=True)
    ativo = models.BooleanField("Ativo", default=True)

    def __str__(self):
        return f"{self.nome} - {self.get_grupo_muscular_principal_display()}"

    class Meta:
        db_table = 'exercicios'
        verbose_name = 'Exercício'
        verbose_name_plural = 'Exercícios'
        ordering = ['nome']
