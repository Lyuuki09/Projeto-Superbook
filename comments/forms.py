from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'conteudo']
        widgets = {
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu comentário...',
                'rows': 3
            })
        }
        labels = {
            'autor': 'Nome',
            'conteudo': 'Comentário'
        }
