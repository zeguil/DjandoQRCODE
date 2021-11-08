from django.urls import path
from . import views

urlpatterns = [
    path('ler/', views.leitor, name='leitor'),
]