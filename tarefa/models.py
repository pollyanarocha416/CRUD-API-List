from django.db import models


class ListarTarefa(models.Model):
    """ Criar um model de tarefas que Retorna todas as tarefas da lista."""
    tasks = models.CharField(max_length=30)
    descricao= models.CharField(max_length=45)
    data_criacao = models.DateField()

    def __str__(self) -> str:
        return self.tasks