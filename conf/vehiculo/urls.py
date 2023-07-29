from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings

urlpatterns = [
    path('',views.index_view,name='index'),
    path('vehiculo/add',views.registro_view, name='registro'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('listar/',views.listar_view, name='listar'),
    path('registro/',views.registroUsuario_view, name='registro'),
]
