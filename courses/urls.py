from django.urls import path
from courses import views

app_name = 'courses'

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:pk>/', views.details, name='details')
]