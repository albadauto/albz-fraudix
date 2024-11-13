from django.urls import path
from . import views

urlpatterns = [
    path('', views.motorista_login_home, name='motorista_login_home'),
    path('inserir_alterar_motorista_login/', views.inserir_alterar_motorista_login, name='inserir_alterar_motorista_login'),
    path('excluir_motorista_login/<int:id>', views.excluir_motorista_login, name='excluir_motorista_login'),
    path('buscar_motorista_login/<int:id>', views.buscar_motorista_login, name='buscar_motorista_login'),


]
