# Generated by Django 4.2.1 on 2023-05-30 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listartarefa',
            old_name='nome_tarefa',
            new_name='tasks',
        ),
    ]
