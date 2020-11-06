from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:pk>/', views.texto, name='texto'),
]
