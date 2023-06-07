from django.http import JsonResponse
from rest_framework import viewsets, generics, status
from tarefa.models import ListarTarefa, Usuario, TasksUsuario
from tarefa.serializer import ListarTarefasSerializer, UsuarioSerializer, TasksUsuariosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

class ListasTarefasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = ListarTarefa.objects.all()
    serializer_class = ListarTarefasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['put'])
    def mark_task_as_completed(self, request, pk=None):
        task = self.get_object()
        task.concluída = True
        task.save()
        serializer = self.serializer_class(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


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