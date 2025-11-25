import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'superbook.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@superbook.com', 'admin123')
    print('✅ Superuser "admin" criado com sucesso!')
    print('   Usuário: admin')
    print('   Senha: admin123')
else:
    print('✅ Superuser "admin" já existe')
