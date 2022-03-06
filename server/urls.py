from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.main),
    path('checkroom/', views.checkroom),
    path('getMessages/', views.getMessages),
    path('send/', views.send),
    path('signin', views.sign_in, name='signin'),
    path('signout/', views.sign_out, name='signout'),
    path('callback/', views.callback, name='callback'),
]