# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api', views.view, name='api view'),
]