from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('entrada', Entrada.as_view(), name='entrada'),
    path('salida', Salida.as_view(), name='salida'),
]