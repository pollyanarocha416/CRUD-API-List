from django.contrib import admin
from tarefa.models import ListarTarefa, Usuario

class Listandotarefas(admin.ModelAdmin):
    list_display = ('id', 'tasks', 'descricao', 'data_criacao')
    list_display_links = ('id', 'tasks')
    search_fields = ('tasks',)
    list_per_page = 20
admin.site.register(ListarTarefa, Listandotarefas)

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'email', 'tarefa')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Usuario, Usuarios)