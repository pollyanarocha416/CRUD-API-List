from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import ListarTarefa, Usuario, TasksUsuario
from tarefa.serializer import ListarTarefasSerializer, UsuarioSerializer, TasksUsuariosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class ListasTarefasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = ListarTarefa.objects.all()
    serializer_class = ListarTarefasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class TasksUsuariosView(generics.ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Usuario.objects.filter(id=id)