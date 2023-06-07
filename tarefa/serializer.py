from rest_framework import serializers, generics
from tarefa.models import ListarTarefa, Usuario, TasksUsuario

class ListarTarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListarTarefa
        fields = ['id', 'tasks', 'descricao', 'data_criacao', 'concluida']

class UsuarioSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    tarefas = ListarTarefasSerializer(many=True, read_only=True)
    
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'idade', 'email', 'tarefa', 'tasks', 'tarefas']
    
    def get_tasks(self, obj):
        return [tarefa.tasks for tarefa in obj.tarefa.all()] if obj.tarefa.exists() else None

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TasksUsuariosSerializer(serializers.ModelSerializer):
    usuarios = UsuarioSerializer(many=True, read_only=True)

    class Meta:
        model = TasksUsuario
        fields = ['id', 'usuarios', 'tasks']