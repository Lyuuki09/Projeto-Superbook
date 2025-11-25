import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superbook.settings')
django.setup()

from heroes.models import Hero
from villains.models import Villain
from posts.models import Post

# Verificar e criar alguns dados de teste
print("\n" + "="*60)
print("🔧 CRIANDO DADOS DE TESTE PARA O ADMIN")
print("="*60 + "\n")

# Criar heróis de teste
heroes_data = [
    {
        'codinome': 'Homem-Aranha',
        'nome_real': 'Peter Parker',
        'poder_principal': 'Teia aracnídea',
        'cidade': 'Nova York',
        'historia': 'Jovem herói com superpoderes após mordida de aranha radioativa.',
        'email_contato': 'peter@avengers.com'
    },
    {
        'codinome': 'Mulher-Maravilha',
        'nome_real': 'Diana Prince',
        'poder_principal': 'Super força',
        'cidade': 'Themyscira',
        'historia': 'Princesa amazona que veio para proteger a Terra.',
        'email_contato': 'diana@justice-league.com'
    }
]

for hero_data in heroes_data:
    hero, created = Hero.objects.get_or_create(
        codinome=hero_data['codinome'],
        defaults=hero_data
    )
    if created:
        print(f"✅ Herói criado: {hero.codinome}")
    else:
        print(f"ℹ️  Herói já existe: {hero.codinome}")

# Criar vilões de teste
villains_data = [
    {
        'codinome': 'Doutor Octávio',
        'nome_real': 'Otto Octavius',
        'poder_principal': 'Tentáculos mecânicos',
        'cidade': 'Nova York',
        'historia': 'Cientista que se tornou um vilão após experimento fracassado.',
        'email_contato': 'otto@oscorp.com'
    },
    {
        'codinome': 'Ares',
        'nome_real': 'Unknown',
        'poder_principal': 'Dominação de guerra',
        'cidade': 'Themyscira',
        'historia': 'Deus da guerra que desafia os deuses.',
        'email_contato': 'ares@olympus.com'
    }
]

for villain_data in villains_data:
    villain, created = Villain.objects.get_or_create(
        codinome=villain_data['codinome'],
        defaults=villain_data
    )
    if created:
        print(f"✅ Vilão criado: {villain.codinome}")
    else:
        print(f"ℹ️  Vilão já existe: {villain.codinome}")

# Criar posts de teste
spiderman = Hero.objects.filter(codinome='Homem-Aranha').first()
if spiderman and Post.objects.filter(autor=spiderman).count() == 0:
    post = Post.objects.create(
        autor=spiderman,
        mensagem='Patrulhando Nova York em mais uma noite! Com grandes poderes vem grande responsabilidade! 🕷️'
    )
    print(f"✅ Post criado para {spiderman.codinome}")
else:
    print("ℹ️  Posts do Homem-Aranha já existem")

print("\n" + "="*60)
print("📊 ACESSE O PAINEL ADMIN")
print("="*60)
print("URL: http://127.0.0.1:8000/admin/")
print("Usuário: admin")
print("Senha: admin123")
print("="*60 + "\n")
