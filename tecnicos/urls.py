from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('tecnicos/', views.TecnicosList.as_view(), name='tecnicos_list'),
    path('tecnicos/create/', views.TecnicosCreate.as_view(), name='tecnicos_create'),
    path('tecnicos/<int:pk>/detail/', views.TecnicosDetail.as_view(), name='tecnicos_detail'),
    path('tecnicos/<int:pk>/update/', views.TecnicosUpdate.as_view(), name='tecnicos_update'),
    path('tecnicos/<int:pk>/delete/', views.TecnicosDelete.as_view(), name='tecnicos_delete'),

]

