from django.contrib import admin
from django.urls import path, include
from tarefa.views import ListasTarefasViewSet, ListarTarefa
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', ListasTarefasViewSet, basename='Tarefas')

urlpatterns = [
#    path('', index, name='index'),
    path('', include(router.urls)),
]