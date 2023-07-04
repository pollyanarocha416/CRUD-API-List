from rest_framework import serializers, generics
from tarefa.models import ListarTarefa, Usuario
from datetime import date

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



class UsuarioTarefaSerializer(serializers.ModelSerializer):
    
    class Meta:
       
        model = Usuario
        fields = ['id', 'nome', 'idade', 'email']

class UsuariosTarefaView(generics.ListAPIView):
   
    def get_serializer_class(self):
      
        if 'tarefa_id' in self.kwargs:
            return UsuarioTarefaSerializer
        
        else:
            return UsuarioSerializer

    def get_queryset(self):
      
        tarefa_id = self.kwargs.get('tarefa_id')
        
        if tarefa_id:
            return Usuario.objects.filter(tarefa=tarefa_id)
        
        else:
            return Usuario.objects.all()


class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListarTarefa
        fields = ['tasks', 'vencimento']

class TarefasProximasVencimentoAPIView(generics.ListAPIView):
    serializer_class = TarefaSerializer

    def get_queryset(self):
        hoje = date.today()
        queryset = ListarTarefa.objects.filter(vencimento__gte=hoje)
        return queryset

class TarefasVencidasAPIView(generics.ListAPIView):
    serializer_class = TarefaSerializer

    def get_queryset(self):
        hoje = date.today()
        queryset = ListarTarefa.objects.filter(vencimento__lt=hoje)
        return queryset
