from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_posts, name='hello_posts'),
    path('lista/', views.PostListView.as_view(), name='lista_posts'),
    path('novo/', views.PostCreateView.as_view(), name='criar_post'),
    path('<int:pk>/', views.post_detail_fbv, name='post_detail'),
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='editar_post'),
    path('<int:pk>/excluir/', views.PostDeleteView.as_view(), name='excluir_post'),
    path('cbv-lista/', views.PostListView.as_view(), name='cbv_lista_posts'),
]