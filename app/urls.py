from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('chamados.urls')),
    path('', include('clientes.urls')),
    path('', include('tecnicos.urls')),

    path('api/v1/', include('authentication.urls')),
]
