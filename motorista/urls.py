from django.urls import path
from . import views
urlpatterns = [
    path('', views.motorista_home, name='motorista_home'),
    path('inserir_motorista/', views.inserir_motorista, name='inserir_motorista'),
    path('deletar_motorista/<int:id>', views.deletar_motorista, name='deletar_motorista'),
]
