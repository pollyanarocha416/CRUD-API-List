# Generated by Django 4.2.1 on 2023-06-05 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0004_remove_usuario_senha_alter_usuario_tarefa'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.listartarefa')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefa.usuario')),
            ],
        ),
    ]