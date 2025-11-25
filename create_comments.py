import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superbook.settings')
django.setup()

from posts.models import Post
from comments.models import Comentario

print("\n" + "="*60)
print("🔧 ADICIONANDO COMENTÁRIOS DE TESTE")
print("="*60 + "\n")

# Obter o primeiro post
post = Post.objects.first()

if post:
    # Criar alguns comentários de teste
    comentarios_data = [
        {
            'autor': 'João Silva',
            'conteudo': 'Excelente post! Adorei a história.'
        },
        {
            'autor': 'Maria Santos',
            'conteudo': 'Muito bom mesmo! Queremos mais histórias como essa.'
        },
        {
            'autor': 'Pedro Costa',
            'conteudo': 'Parabéns pelo trabalho! Você é incrível.'
        }
    ]

    for comentario_data in comentarios_data:
        comentario, created = Comentario.objects.get_or_create(
            post=post,
            autor=comentario_data['autor'],
            defaults={'conteudo': comentario_data['conteudo']}
        )
        if created:
            print(f"✅ Comentário criado de {comentario.autor}")
        else:
            print(f"ℹ️  Comentário já existe de {comentario.autor}")

    print(f"\n📊 Post tem {post.comentarios.count()} comentário(s)")
else:
    print("⚠️  Nenhum post encontrado. Crie um post primeiro no admin.")

print("\n" + "="*60)
print("✅ TESTE OS ENDPOINTS:")
print("="*60)
print("Lista de Posts: http://127.0.0.1:8000/posts/lista/")
print("Novo Post: http://127.0.0.1:8000/posts/novo/")
print("Admin: http://127.0.0.1:8000/admin/")
print("="*60 + "\n")
