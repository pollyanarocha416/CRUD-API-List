from rest_framework import serializers
from tarefa.models import ListarTarefa

class ListarTarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListarTarefa
        fields = ['id', 'tasks', 'descricao', 'data_criacao']

