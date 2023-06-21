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
        return [tarefa.tasks for tarefa in obj.tarefa.all()] if obj.tarefa.exists() else None

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

""" class TasksUsuariosSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='usuarios.nome')
    idade = serializers.IntegerField(source='usuarios.idade')


    class Meta:
        model = TasksUsuario
        fields = ['id', 'nome', 'idade']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            key: representation[key]
            for key in representation
                if key in ['id', 'nome', 'idade']
        } """