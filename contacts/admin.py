from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'relationship', 'phone', 'email', 'created_at']
    list_filter = ['relationship', 'created_at']
    search_fields = ['name', 'relationship', 'phone', 'email']
    list_per_page = 20
    ordering = ['name']
