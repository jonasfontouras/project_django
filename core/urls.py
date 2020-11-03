from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.ayurveda_site, name='index'),
]
