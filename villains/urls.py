from django.urls import path
from . import views

urlpatterns = [
    path('', views.VillainListView.as_view(), name='lista_viloes'),
    path('novo/', views.VillainCreateView.as_view(), name='criar_vilao'),
    path('<int:pk>/', views.VillainDetailView.as_view(), name='vilao_detail'),
    path('<int:pk>/editar/', views.VillainUpdateView.as_view(), name='editar_vilao'),
    path('<int:pk>/excluir/', views.VillainDeleteView.as_view(), name='excluir_vilao'),
]
