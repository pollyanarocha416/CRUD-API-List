from django.http import JsonResponse
from rest_framework import viewsets
from tarefa.models import ListarTarefa
from tarefa.serializer import ListarTarefasSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ListasTarefasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = ListarTarefa.objects.all()
    serializer_class = ListarTarefasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
