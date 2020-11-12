from django.urls import path, re_path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>/', views.details, name='details'),
]
