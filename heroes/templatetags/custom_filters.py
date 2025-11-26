from django import template

register = template.Library()

@register.filter
def add_class(value, arg):
    """
    Adiciona uma classe CSS a um campo de formulário do Django.
    Uso: {{ field|add_class:"form-control" }}
    """
    return value.as_widget(attrs={"class": arg})


@register.filter
def has_hero(user):
    """Retorna True se o usuário autenticado possui objeto related `hero`."""
    if not user or not getattr(user, 'is_authenticated', False):
        return False
    try:
        return user.hero is not None
    except Exception:
        return False
