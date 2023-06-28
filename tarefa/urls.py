from django.contrib import admin
from django.urls import path, include
from tarefa.views import ListasTarefasViewSet, UsuarioViewSet, TarefasConcluidasView, ApiRootViewSet, TarefasConcluidasViewSet
from rest_framework import routers
from tarefa.serializer import UsuarioCreateView, UsuariosTarefaView


router = routers.DefaultRouter()
router.register('tasks', ListasTarefasViewSet, basename='Tarefas')
router.register('usuario', UsuarioViewSet, basename='Usuario')
router.register('tasks_concluidas',TarefasConcluidasViewSet, basename='tasks_concluidas')

urlpatterns = [
    path('', include(router.urls)),
    path('usuario/', UsuarioCreateView.as_view(), name='criar-usuario'),
    path('tasks/<int:tarefa_id>/usuarios/', UsuariosTarefaView.as_view(), name='usuarios_tarefa'),
    path('', ApiRootViewSet.as_view({'get': 'list'}), name='api-root'),
    path('tarefas/concluidas/', TarefasConcluidasView.as_view(), name='tarefas-concluidas'),
]