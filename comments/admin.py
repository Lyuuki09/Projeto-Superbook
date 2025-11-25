from django.contrib import admin
from .models import Comentario


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'post', 'conteudo_resumido', 'criado_em']
    list_filter = ['criado_em', 'post']
    search_fields = ['autor', 'conteudo', 'post__id']
    readonly_fields = ['criado_em', 'atualizado_em']

    fieldsets = (
        ('Informações do Comentário', {
            'fields': ('post', 'autor')
        }),
        ('Conteúdo', {
            'fields': ('conteudo',)
        }),
        ('Dados de Registro', {
            'fields': ('criado_em', 'atualizado_em')
        }),
    )

    def conteudo_resumido(self, obj):
        return obj.conteudo[:50] + '...' if len(obj.conteudo) > 50 else obj.conteudo
    conteudo_resumido.short_description = 'Conteúdo'
