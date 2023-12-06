from django.shortcuts import render
from django.http import HttpResponse

from flia.models import Parient

def create_parient(request):
    new_parient = Parient.objects.create(name='Pedro',dni=12314,live =False)
    print(new_parient)
    return HttpResponse('Se creo el nuevo pariente')

def list_parients(request):
    all_parient = Parient.objects.all()
    print(all_parient)
    context = {
        'parients':all_parient,
    }
    return render(request,'list_parients.html',context=context)
