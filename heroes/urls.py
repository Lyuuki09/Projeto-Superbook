from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_heroes, name='hello_heroes'),
    path('lista/', views.lista_herois, name='lista_herois'),
    path('cbv-lista/', views.HeroListView.as_view(), name='cbv_lista_herois'),
]
