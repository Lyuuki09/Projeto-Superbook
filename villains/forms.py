from django import forms
from .models import Villain


class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'historia', 'email_contato', 'imagem']
        widgets = {
            'codinome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Doutor Mal'}),
            'nome_real': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João Silva'}),
            'poder_principal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Teletransporte'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Gotham'}),
            'historia': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Conte a história do vilão...'}),
            'email_contato': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'imagem': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
