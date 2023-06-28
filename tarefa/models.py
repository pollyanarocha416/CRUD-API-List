from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ListarTarefa(models.Model):
    
    """ Criar um model de tarefas que Retorna todas as tarefas da lista."""
    
    tasks = models.CharField(max_length=30)
    descricao= models.CharField(max_length=45)
    data_criacao = models.DateField()#    YYYY-MM-DD.
    vencimento = models.DateField(default='2023-01-01')
    concluida = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.tasks
    
    def status(self):
        if self.concluida:
            return "concluída"
        else:
            return "pendente"

class Usuario(models.Model):
    
    """Criar um model de usuario que retorna o usuario e quais sao as tarefas dele"""
    
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    email = models.EmailField(max_length=254)
    tarefa = models.ManyToManyField(ListarTarefa, related_name='usuarios', default='valor_padrao')# remover a tarefa dele se ele for excluido
