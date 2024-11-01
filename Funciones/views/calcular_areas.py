from django.shortcuts import render

def calcular_areas(request):
    return render(request, 'calcular_areas.html')
