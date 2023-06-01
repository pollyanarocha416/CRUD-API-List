from django.contrib import admin
from django.urls import path, include
from tarefa.views import ListasTarefasViewSet, UsuarioViewSet
from rest_framework import routers
from tarefa.serializer import UsuarioCreateView

router = routers.DefaultRouter()
router.register('tasks', ListasTarefasViewSet, basename='Tarefas')
router.register('usuario', UsuarioViewSet, basename='Usuario')

urlpatterns = [
#    path('', index, name='index'),
    path('', include(router.urls)),
    path('usuario/', UsuarioCreateView.as_view(), name='criar-usuario'),
]