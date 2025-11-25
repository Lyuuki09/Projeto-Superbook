from django import forms
from .models import Hero


class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, required=True, label="Seu nome")
    email = forms.EmailField(required=True, label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea, required=True, label="Mensagem")


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'historia']
