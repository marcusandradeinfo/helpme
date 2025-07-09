from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.ClientesList.as_view(), name='clientes_list'),
    path('clientes/create/', views.ClientesCreate.as_view(), name='clientes_create'),
    path('clientes/<int:pk>/detail/', views.ClientesDetail.as_view(), name='clientes_detail'),
    path('clientes/<int:pk>/update/', views.ClientesUpdate.as_view(), name='clientes_update'),
    path('clientes/<int:pk>/delete/', views.ClientesDelete.as_view(), name='clientes_delete'),

]