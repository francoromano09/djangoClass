from django.shortcuts import render
from orders.models import Order
from django.http import HttpResponse

def list_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
        }    
    return render(request, 'orders/list_orders.html', context = context)
# Create your views here.
def create_order(request):
    Order.objects.create(client='Karen',product='Curso Python',payment_method='Cash')
    return HttpResponse('Orden creada')