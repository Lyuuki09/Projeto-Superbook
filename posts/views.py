from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .models import Post, Like
from .forms import PostForm
from heroes.models import Hero


def hello_posts(request):
    return render(request, None) if False else (getattr(request, 'META', None) and (None))


class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
    ordering = ['-criado_em']

    def get_queryset(self):
        return Post.objects.all().select_related('autor')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

    def form_valid(self, form):
        # Garante que usuário tem Hero vinculado
        hero = getattr(self.request.user, 'hero', None)
        if not hero:
            messages.error(self.request, "Crie seu perfil de herói antes de publicar.")
            return redirect('criar_heroi')
        form.instance.autor = hero
        messages.success(self.request, "Post criado com sucesso.")
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/form_post.html'
    success_url = reverse_lazy('lista_posts')

    def test_func(self):
        obj = self.get_object()
        try:
            return self.request.user.is_authenticated and obj.autor == self.request.user.hero
        except Hero.DoesNotExist:
            return False

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para editar este post.")
        return redirect('lista_posts')


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_posts')

    def test_func(self):
        obj = self.get_object()
        try:
            return self.request.user.is_authenticated and obj.autor == self.request.user.hero
        except Hero.DoesNotExist:
            return False

    def handle_no_permission(self):
        messages.error(self.request, "Você não tem permissão para excluir este post.")
        return redirect('lista_posts')


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
    from comments.models import Comentario
    from comments.forms import ComentarioForm

    post = get_object_or_404(Post.objects.select_related('autor'), pk=pk)
    comentarios = Comentario.objects.filter(post=post).order_by('-criado_em')
    form_comentario = ComentarioForm()

    if request.method == 'POST':
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            comentario = form_comentario.save(commit=False)
            comentario.post = post
            comentario.save()
            messages.success(request, "Comentário adicionado.")
            return redirect('post_detail', pk=pk)

    context = {
        'post': post,
        'comentarios': comentarios,
        'form_comentario': form_comentario
    }

    return render(request, 'posts/post_detail.html', context)


def criar_post(request):
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


@login_required
def toggle_pow(request, pk):
    post = get_object_or_404(Post, pk=pk)
    hero = getattr(request.user, 'hero', None)
    if not hero:
        messages.error(request, "Crie seu herói antes de curtir.")
        return redirect('criar_heroi')

    like, created = Like.objects.get_or_create(post=post, heroi=hero)
    if not created:
        like.delete()

    # Redireciona de volta (referer) ou para lista como fallback
    return redirect(request.META.get('HTTP_REFERER', reverse('lista_posts')))