from django.urls import path
from . import views
urlpatterns = [
    path('', views.motorista_home, name='motorista_home')
]
