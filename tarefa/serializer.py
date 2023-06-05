from rest_framework import serializers, generics
from tarefa.models import ListarTarefa, Usuario, TasksUsuario

class ListarTarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListarTarefa
        fields = ['id', 'tasks', 'descricao', 'data_criacao']

class UsuarioSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'idade', 'email', 'tarefa', 'tasks']

    def get_tasks(self, obj):
        return obj.tarefa.tasks if obj.tarefa else None

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TasksUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksUsuario
        fields = ['id', 'tarefas', 'usuarios']