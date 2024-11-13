from django.urls import path
from . import views

urlpatterns = [
    path('', views.motorista_login_home, name='motorista_login_home')
]
