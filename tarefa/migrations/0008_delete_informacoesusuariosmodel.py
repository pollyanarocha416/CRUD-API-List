# Generated by Django 4.2.1 on 2023-06-07 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0007_rename_tarefas_tasksusuario_tasks_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InformacoesUsuariosModel',
        ),
    ]
