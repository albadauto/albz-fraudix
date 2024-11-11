from django.urls import path
from . import views

urlpatterns = [
    path('', views.historico_home, name='historico_home')
]
