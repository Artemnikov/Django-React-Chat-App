from django.urls import path

from . import views

urlpatterns = [
    path('', views.main),
    path('checkroom/', views.checkroom),
    path('getMessages/', views.getMessages),
    path('send/', views.send),
]