from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lobby', views.index, name='room'),
    path('room', views.index, name='room'),
    path('send/', views.index),
    path('proccess/', views.index),
]