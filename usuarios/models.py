from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Usuario(AbstractUser):
    # Dados pessoais
    data_nascimento = models.DateField("Data de Nascimento", null=True, blank=True)

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    genero = models.CharField("Gênero", max_length=1, choices=GENERO_CHOICES, null=True, blank=True)

    # Dados físicos
    altura = models.FloatField(
        "Altura (metros)",
        null=True,
        blank=True,
        validators=[MinValueValidator(0.5), MaxValueValidator(3.0)]
    )
    peso_atual = models.FloatField(
        "Peso Atual (kg)",
        null=True,
        blank=True,
        validators=[MinValueValidator(20.0), MaxValueValidator(500.0)]
    )

    # Objetivos fitness
    OBJETIVO_CHOICES = [
        ('perda_peso', 'Perda de Peso'),
        ('ganho_massa', 'Ganho de Massa Muscular'),
        ('manutencao', 'Manutenção da Saúde'),
        ('performance', 'Melhoria de Performance'),
        ('reabilitacao', 'Reabilitação'),
    ]
    objetivo_principal = models.CharField(
        "Objetivo Principal",
        max_length=50,
        choices=OBJETIVO_CHOICES,
        default='manutencao'
    )

    NIVEL_CHOICES = [
        ('iniciante', 'Iniciante'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
        ('profissional', 'Profissional'),
    ]
    nivel_experiencia = models.CharField(
        "Nível de Experiência",
        max_length=20,
        choices=NIVEL_CHOICES,
        default='iniciante'
    )

    bio = models.TextField("Biografia", blank=True, max_length=500)
    data_ultima_atividade = models.DateTimeField("Última Atividade", auto_now=True)

    @property
    def idade(self):
        if self.data_nascimento:
            today = timezone.now().date()
            return today.year - self.data_nascimento.year - (
                (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
            )
        return None

    @property
    def imc(self):
        if self.peso_atual and self.altura:
            return round(self.peso_atual / (self.altura ** 2), 2)
        return None

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
