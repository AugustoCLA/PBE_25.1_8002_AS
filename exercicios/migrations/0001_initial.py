# Generated by Django 5.2.1 on 2025-06-23 06:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome do Exercício')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('grupo_muscular_principal', models.CharField(choices=[('peito', 'Peitoral'), ('costas', 'Costas'), ('ombros', 'Ombros'), ('biceps', 'Bíceps'), ('triceps', 'Tríceps'), ('quadriceps', 'Quadríceps'), ('posterior_coxa', 'Posterior de Coxa'), ('gluteos', 'Glúteos'), ('panturrilha', 'Panturrilha'), ('core', 'Core/Abdômen'), ('cardio', 'Cardiovascular')], max_length=50, verbose_name='Grupo Muscular Principal')),
                ('equipamento_necessario', models.CharField(choices=[('peso_corporal', 'Peso Corporal'), ('halteres', 'Halteres'), ('barra', 'Barra'), ('maquina', 'Máquina'), ('cabo', 'Cabo/Polia'), ('kettlebell', 'Kettlebell'), ('elastico', 'Elástico'), ('medicine_ball', 'Medicine Ball'), ('outros', 'Outros')], default='peso_corporal', max_length=50, verbose_name='Equipamento Necessário')),
                ('nivel_dificuldade', models.CharField(choices=[('iniciante', 'Iniciante'), ('intermediario', 'Intermediário'), ('avancado', 'Avançado')], default='iniciante', max_length=20, verbose_name='Nível de Dificuldade')),
                ('instrucoes_execucao', models.TextField(verbose_name='Instruções de Execução')),
                ('calorias_por_minuto', models.FloatField(default=5.0, validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(50.0)], verbose_name='Calorias por Minuto')),
                ('tempo_execucao_medio', models.PositiveIntegerField(default=60, verbose_name='Tempo Médio de Execução (segundos)')),
                ('publico', models.BooleanField(default=True, verbose_name='Público')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Exercício',
                'verbose_name_plural': 'Exercícios',
                'db_table': 'exercicios',
                'ordering': ['nome'],
            },
        ),
    ]
