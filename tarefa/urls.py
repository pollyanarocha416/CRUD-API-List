from django.contrib import admin
from django.urls import path, include
from tarefa.views import ListasTarefasViewSet, UsuarioViewSet, TarefasConcluidasView, ApiRootViewSet
from rest_framework import routers
from tarefa.serializer import UsuarioCreateView


router = routers.DefaultRouter()
router.register('tasks', ListasTarefasViewSet, basename='Tarefas')
router.register('usuario', UsuarioViewSet, basename='Usuario')

urlpatterns = [
    path('', include(router.urls)),
    path('usuario/', UsuarioCreateView.as_view(), name='criar-usuario'),
#    path('tasks/<int:tarefa>/usuarios/', TasksUsuariosView.as_view(), name='tasks-usuarios'),
    path('', ApiRootViewSet.as_view({'get': 'list'}), name='api-root'),
    path('tarefas/concluidas/', TarefasConcluidasView.as_view(), name='tarefas-concluidas'),
]