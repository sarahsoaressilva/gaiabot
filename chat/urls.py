# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='index'),
    path('enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]