from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Villain
from .forms import VillainForm


class VillainListView(ListView):
    model = Villain
    template_name = 'villains/lista_viloes.html'
    context_object_name = 'viloes'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_viloes'] = Villain.objects.count()
        return context


class VillainCreateView(CreateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_vilao.html'
    success_url = reverse_lazy('lista_viloes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Criar Novo Vilão'
        context['botao'] = 'Criar Vilão'
        return context


class VillainDetailView(DetailView):
    model = Villain
    template_name = 'villains/detalhe_vilao.html'
    context_object_name = 'vilao'


class VillainUpdateView(UpdateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_vilao.html'
    success_url = reverse_lazy('lista_viloes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = f'Editar {self.object.codinome}'
        context['botao'] = 'Atualizar Vilão'
        return context


class VillainDeleteView(DeleteView):
    model = Villain
    template_name = 'villains/confirmar_exclusao_vilao.html'
    success_url = reverse_lazy('lista_viloes')
    context_object_name = 'vilao'
