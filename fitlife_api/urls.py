from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.views import UsuarioViewSet
from treinos.views import TreinoViewSet, TreinoExercicioViewSet
from exercicios.views import ExercicioViewSet

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'treinos', TreinoViewSet)
router.register(r'treinos-exercicios', TreinoExercicioViewSet)
router.register(r'exercicios', ExercicioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
