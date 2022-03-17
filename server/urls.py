from django.urls import path
from . import views

urlpatterns = [
    path('checkroom', views.checkroom),
    path('getMessages/', views.getMessages),
    path('send', views.send),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('getAToken/', views.callback, name='callback'),
    path('verifyjwt', views.validate, name='validate'),
]