# Generated by Django 4.2.1 on 2023-06-06 14:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tarefa.models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0006_remove_usuario_tarefa_usuario_tarefa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasksusuario',
            old_name='tarefas',
            new_name='tasks',
        ),
        migrations.CreateModel(
            name='InformacoesUsuariosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name=tarefa.models.Usuario)),
                ('idade', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)], verbose_name=tarefa.models.Usuario)),
                ('email', models.EmailField(max_length=254, verbose_name=tarefa.models.Usuario)),
                ('tasks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.listartarefa')),
            ],
        ),
    ]
