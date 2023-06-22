from rest_framework import serializers, generics
from tarefa.models import ListarTarefa, Usuario


class ListarTarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListarTarefa
        fields = ['id', 'tasks', 'descricao', 'data_criacao', 'vencimento', 'concluida']

class UsuarioSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    tarefas = ListarTarefasSerializer(many=True, read_only=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'idade', 'email', 'tarefa', 'tasks', 'tarefas']
    
    def get_tasks(self, obj):
        return [tarefa.id for tarefa in obj.tarefa.all()] if obj.tarefa.exists() else None


class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuariosTarefaView(generics.ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        tarefa_id = self.kwargs['tarefa_id']
        return Usuario.objects.filter(tarefa=tarefa_id)