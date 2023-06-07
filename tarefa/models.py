from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class ListarTarefa(models.Model):
    """ Criar um model de tarefas que Retorna todas as tarefas da lista."""
    tasks = models.CharField(max_length=30)
    descricao= models.CharField(max_length=45)
    data_criacao = models.DateField()

    def __str__(self) -> str:
        return self.tasks

class Usuario(models.Model):
    """Criar um model de usuario que retorna o usuario e quais sao as tarefas dele"""
    nome = models.CharField(max_length=30)
    idade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    email = models.EmailField(max_length=254)
    tarefa = models.ManyToManyField(ListarTarefa, related_name='usuarios')# remover a tarefa dele se ele for excluido

class TasksUsuario(models.Model):
    """Model de quais são os usuarios de determinada tasks"""
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tasks = models.ForeignKey(ListarTarefa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.usuarios