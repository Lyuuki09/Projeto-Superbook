from django.contrib import admin
from .models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'autor_codinome', 'mensagem_resumida', 'criado_em']
    list_filter = ['criado_em', 'autor']
    search_fields = ['autor__codinome', 'mensagem']
    readonly_fields = ['criado_em']

    fieldsets = (
        ('Autor', {
            'fields': ('autor',)
        }),
        ('Conteúdo', {
            'fields': ('mensagem',)
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )

    def autor_codinome(self, obj):
        return obj.autor.codinome
    autor_codinome.short_description = 'Herói Autor'

    def mensagem_resumida(self, obj):
        return obj.mensagem[:50] + '...' if len(obj.mensagem) > 50 else obj.mensagem
    mensagem_resumida.short_description = 'Mensagem'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'heroi_codinome', 'post_id', 'criado_em']
    list_filter = ['criado_em', 'heroi']
    search_fields = ['heroi__codinome', 'post__id']
    readonly_fields = ['criado_em']

    def heroi_codinome(self, obj):
        return obj.heroi.codinome
    heroi_codinome.short_description = 'Herói'
