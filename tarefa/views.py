from django.http import JsonResponse
from rest_framework import viewsets, generics
from tarefa.models import ListarTarefa
from tarefa.serializer import ListarTarefasSerializer

class ListasTarefasViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = ListarTarefa.objects.all()
    serializer_class = ListarTarefasSerializer