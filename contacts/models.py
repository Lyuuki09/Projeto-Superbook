from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    relationship = models.CharField(max_length=50, blank=True, null=True, verbose_name="Relacionamento")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ['name']

    def __str__(self):
        return self.name
