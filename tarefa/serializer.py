from rest_framework import serializers, generics
from tarefa.models import ListarTarefa, Usuario, TasksUsuario

class ListarTarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListarTarefa
        fields = ['id', 'tasks', 'descricao', 'data_criacao']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'idade', 'email', 'tarefa']

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class TasksUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksUsuario
        fields = ['id', 'tarefas', 'usuarios']