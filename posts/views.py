from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from heroes.models import Hero

def hello_posts(request):
    return HttpResponse("Bem-vindo ao módulo Posts!")

# Generic Class-Based Views para CRUD de Posts
class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        return Post.objects.all().select_related('autor')


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')
    
    def form_valid(self, form):
        post = form.save(commit=False)
        # Atribuir primeiro herói disponível como autor
        herois = Hero.objects.all()
        if herois.exists():
            post.autor = herois.first()
        post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.select_related('autor')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Importar aqui para evitar import circular
        from comments.models import Comentario
        from comments.forms import ComentarioForm
        
        context['comentarios'] = Comentario.objects.filter(post=self.object)
        context['form_comentario'] = ComentarioForm()
        return context


def post_detail_fbv(request, pk):
    """
    View baseada em função (FBV) para exibir detalhe do post com comentários.
    Permite adicionar novos comentários via POST.
    """
    from comments.models import Comentario
    from comments.forms import ComentarioForm
    
    # Buscar o post ou retornar 404
    post = get_object_or_404(Post.objects.select_related('autor'), pk=pk)
    
    # Buscar comentários do post
    comentarios = Comentario.objects.filter(post=post).order_by('-criado_em')
    
    # Inicializar o formulário de comentário
    form_comentario = ComentarioForm()
    
    # Processar novo comentário se for POST
    if request.method == 'POST':
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            # Criar comentário sem salvar (commit=False)
            comentario = form_comentario.save(commit=False)
            # Associar o comentário ao post
            comentario.post = post
            # Salvar no banco
            comentario.save()
            # Redirecionar para a mesma página
            return redirect('post_detail', pk=pk)
    
    context = {
        'post': post,
        'comentarios': comentarios,
        'form_comentario': form_comentario
    }
    
    return render(request, 'posts/post_detail.html', context)


def criar_post(request):
    """View baseada em função - mantida para compatibilidade"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            herois = Hero.objects.all()
            if herois.exists():
                post.autor = herois.first()
            post.save()
            return redirect('lista_posts')
    else:
        form = PostForm()
    return render(request, "posts/form_post.html", {"form": form})