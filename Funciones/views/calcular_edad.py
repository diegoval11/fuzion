from django.shortcuts import render
from datetime import datetime

def calcular_edad(request):
    edad = None
    name = None
    if request.method == 'POST':
        name = request.POST['name']
        birthdate_str = request.POST['birthdate']
        try:
            birthdate = datetime.strptime(birthdate_str, '%d/%m/%Y')
            today = datetime.today()
            edad = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        except ValueError:
            edad = 'Fecha de nacimiento inválida. Use el formato DD/MM/YYYY.'
    return render(request, 'calcular_edad.html', {'edad': edad, 'name': name})
