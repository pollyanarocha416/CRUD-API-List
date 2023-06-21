# Generated by Django 4.2.1 on 2023-06-21 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0008_remove_tasksusuario_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='listartarefa',
            name='vencimento',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AddField(
            model_name='tasksusuario',
            name='tarefa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tarefa.listartarefa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tarefa',
            field=models.ManyToManyField(default='valor_padrao', related_name='usuarios', to='tarefa.listartarefa'),
        ),
    ]
