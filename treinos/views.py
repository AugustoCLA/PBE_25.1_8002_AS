from rest_framework import viewsets
from .models import Treino, TreinoExercicio
from .serializers import TreinoSerializer, TreinoExercicioSerializer

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer

class TreinoExercicioViewSet(viewsets.ModelViewSet):
    queryset = TreinoExercicio.objects.all()
    serializer_class = TreinoExercicioSerializer


