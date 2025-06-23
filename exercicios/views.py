from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from .models import Exercicio
from .serializers import ExercicioSerializer


class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.filter(ativo=True)
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        'grupo_muscular_principal',
        'equipamento_necessario',
        'nivel_dificuldade'
    ]
    search_fields = ['nome', 'descricao']
    ordering_fields = ['nome', 'data_criacao', 'calorias_por_minuto']
    ordering = ['nome']
