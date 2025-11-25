from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'email_contato', 'criado_em']
    list_filter = ['cidade', 'criado_em']
    search_fields = ['codinome', 'nome_real', 'cidade', 'email_contato']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real', 'email_contato', 'imagem')
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']
