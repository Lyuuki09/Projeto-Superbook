from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

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