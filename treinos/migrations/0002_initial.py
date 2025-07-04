# Generated by Django 5.2.1 on 2025-06-23 06:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exercicios', '0002_initial'),
        ('treinos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='treino',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treinos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='treinoexercicio',
            name='exercicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercicios.exercicio'),
        ),
        migrations.AddField(
            model_name='treinoexercicio',
            name='treino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='treinos.treino'),
        ),
        migrations.AddField(
            model_name='treino',
            name='exercicios',
            field=models.ManyToManyField(related_name='treinos', through='treinos.TreinoExercicio', to='exercicios.exercicio'),
        ),
    ]
