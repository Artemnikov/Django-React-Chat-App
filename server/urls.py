from django.urls import path
from . import views
from rest_framework_jwt.views import verify_jwt_token, obtain_jwt_token


urlpatterns = [
    path('checkroom', views.checkroom),
    path('getMessages/', views.getMessages),
    path('send', views.send),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.sign_out, name='signout'),
    path('getAToken', views.callback, name='callback'),
    # path('getJWT', obtain_jwt_token, name='getJWT'),
    path('checkJWT', verify_jwt_token )
]
