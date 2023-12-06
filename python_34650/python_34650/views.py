from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse("Hola Mundo")

def otra_mas(request):
    return HttpResponse("Si, Otra mas para el cuaderno")

def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f'La fecha de hoy es {hoy}')

def vista_con_edad(request, edad):

    return HttpResponse(f'Tu edad es {edad}?')

def vista_con_template(request):
    return render(request, 'template.html',context={})

def saludo_desde_template(request):
    context = {
        'nombre':'Franco',
        'edad' : 29,
        'usa_lentes':True,
        'lista':[1,3,5,8,13,20,40,100],
        'lista_frutas': {'manzana','pera','banana'}

    }
    return render(request, 'saludo.html',context=context)