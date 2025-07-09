
from django.contrib import admin
from django.urls import path


from django.urls import path
from . import views

urlpatterns = [
    path('chamados/', views.ChamadosList.as_view(), name='chamados_list'),
    path('chamados/create/', views.ChamadosCreate.as_view(), name='chamados_create'),
    path('chamados/<int:pk>/detail/', views.ChamadosDetail.as_view(), name='chamados_detail'),
    path('chamados/<int:pk>/update/', views.ChamadosUpdate.as_view(), name='chamados_update'),
    path('chamados/<int:pk>/delete/', views.ChamadosDelete.as_view(), name='chamados_delete'),

    path('api/v1/chamados/', views.ChamadosCreateApi.as_view(), name='chamados-create-api')

]
