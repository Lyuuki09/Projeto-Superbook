
from django.db import models
from django.contrib.auth.models import User


class Hero(models.Model):
    # vinculo opcional com User para evitar quebra em migrações iniciais
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hero', null=True, blank=True)

    codinome = models.CharField(max_length=50, unique=True)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    email_contato = models.EmailField(blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos_herois/', blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codinome

