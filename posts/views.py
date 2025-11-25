from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from heroes.models import Hero

def hello_posts(request):
    return HttpResponse("Bem-vindo ao módulo Posts!")

def lista_posts(request):
    posts = Post.objects.all().select_related('autor')
    return render(request, "posts/lista_posts.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        return Post.objects.all().select_related('autor')

def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Você pode atribuir o autor aqui (por enquanto vamos usar o primeiro herói disponível)
            # Em uma aplicação real, você pegaria o usuário autenticado
            herois = Hero.objects.all()
            if herois.exists():
                post.autor = herois.first()
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()

    return render(request, "posts/form_post.html", {"form": form})