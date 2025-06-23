from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
    criado_por_nome = serializers.CharField(
        source='criado_por.get_full_name',
        read_only=True
    )

    class Meta:
        model = Exercicio
        fields = '__all__'
        read_only_fields = ['criado_por', 'data_criacao']

    def create(self, validated_data):
        validated_data['criado_por'] = self.context['request'].user
        return super().create(validated_data)
    

