from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Hero
from .forms import ContatoForm, HeroForm

def hello_heroes(request):
    return HttpResponse("Bem-vindo ao módulo Heroes!")

def lista_herois(request):
    herois = Hero.objects.all()
    return render(request, "heroes/lista_herois.html", {"herois": herois})

class HeroListView(ListView):
    model = Hero
    template_name = "heroes/lista_herois.html"
    context_object_name = "herois"

def contato_view(request):
    form = ContatoForm()

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "heroes/contato_sucesso.html")

    return render(request, "heroes/contato.html", {"form": form})

def criar_heroi(request):
    if request.method == "POST":
        form = HeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_herois')
    else:
        form = HeroForm()

    return render(request, "heroes/form_heroi.html", {"form": form})
