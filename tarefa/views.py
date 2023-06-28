from django.http import JsonResponse
from rest_framework import viewsets, generics, status
from tarefa.models import ListarTarefa, Usuario
from tarefa.serializer import ListarTarefasSerializer, UsuarioSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes, api_view

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

class ApiRootViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {
            "tasks": reverse("Tarefas-list", request=request),
            "usuario": reverse("Usuario-list", request=request),
            "tarefas_concluidas": reverse("tarefas-concluidas", request=request),
        }
        return Response(data)

class TarefasConcluidasView(generics.ListAPIView):
    serializer_class = ListarTarefasSerializer

    def get_queryset(self):
        return ListarTarefa.objects.filter(concluida=True)
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

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

class TarefasConcluidasViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return ListarTarefa.objects.filter(concluida=True)
    queryset = ListarTarefa.objects.all()
    serializer_class = ListarTarefasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

