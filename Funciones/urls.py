from django.urls import path
from .views import home, calculadora, calcular_areas, calcular_edad

urlpatterns = [
    path('', home.index, name='home'),
    path('calculadora/', calculadora.index, name='calculadora'),
    path('calcular_areas/', calcular_areas.calcular_areas, name='calcular_areas'),
    path('calcular_edad/', calcular_edad.calcular_edad, name='calcular_edad'),
    # Agrega aquí más rutas para otras funcionalidades
]
