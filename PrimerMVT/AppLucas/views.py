from django.shortcuts import render
from AppLucas.models import Familiar

# Create your views here.

def familiares(request):
    
    familiar_1 = Familiar(nombre="Lucas Gole", fecha_nacimiento="2022-02-20", documento="123456")
    familiar_1.save()
    familiar_2 = Familiar(nombre="Barbi Gole", fecha_nacimiento="2021-01-10", documento="456789")
    familiar_2.save()
    familiar_3 = Familiar(nombre="Lucho Gole", fecha_nacimiento="2023-03-30", documento="789123")
    familiar_3.save()
    
    contexto = {
        "nombre_1": familiar_1.nombre,
        "fecha_1": familiar_1.fecha_nacimiento,
        "documento_1": familiar_1.documento,
        "nombre_2": familiar_2.nombre,
        "fecha_2": familiar_2.fecha_nacimiento,
        "documento_2": familiar_2.documento, 
        "nombre_3": familiar_3.nombre,
        "fecha_3": familiar_3.fecha_nacimiento,
        "documento_3": familiar_3   .documento,        
    }
    
    return render(request, "familiares.html", contexto)
    
