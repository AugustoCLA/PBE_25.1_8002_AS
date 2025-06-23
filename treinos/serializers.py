from rest_framework import serializers
from .models import Treino, TreinoExercicio

class TreinoExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreinoExercicio
        fields = '__all__'

class TreinoSerializer(serializers.ModelSerializer):
    exercicios = TreinoExercicioSerializer(many=True, read_only=True)

    class Meta:
        model = Treino
        fields = ['id', 'usuario', 'nome', 'descricao', 'exercicios']

