from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from providers.models import Provider
from providers.forms import ProviderForm

def providers_list(request):

    providers = Provider.objects.filter(is_active=True) #Alineacion logica
    context = {
        'providers':providers
    }
    return render(request, 'providers/providers_list.html',context=context)

class ProvidersListView(LoginRequiredMixin,ListView):
    model = Provider
    template_name = 'providers/providers_list.html'
    queryset = Provider.objects.filter(is_active=True)
    
def providers_create(request):
    if request.method == 'GET':
        context = {
            'form' : ProviderForm()
    }
        return render(request, 'providers/create_provider.html',context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
    if form.is_valid():
       #Creamos el producto
        Provider.objects.create(
            name = form.cleaned_data['name'],
            address = form.cleaned_data['address'],
            phone_number = form.cleaned_data['phone_number'],
            email = form.cleaned_data['email'],
            condition = form.cleaned_data['condition'],
        )
        context = {
            'message':'Proveedor creado exitosamente'
        }
    else:
        context = {
            'form_errors': form.errors,
            'form':ProviderForm()
        }
    return render(request, 'providers/create_provider.html',context=context)
        
        #Mostramos el formulario con los errores

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/create_provider.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'

def providers_update(request,pk):
    provider = Provider.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form' : ProviderForm(
                initial = {
                    'name':provider.name,
                    'address':provider.address,
                    'phone_number':provider.phone_number,
                    'email':provider.email,
                    'condition':provider.condition,
                }
            )
    }
        return render(request, 'providers/update_provider.html',context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            #Actualizamos el producto
            provider.name = form.cleaned_data['name']
            provider.address = form.cleaned_data['address']
            provider.phone_number = form.cleaned_data['phone_number']
            provider.email = form.cleaned_data['email']
            provider.condition = form.cleaned_data['condition']
            provider.save()
        context = {
            'message':'Proveedor Actualizado exitosamente'
        }
    else:
        context = {
            'form_errors': form.errors,
            'form':ProviderForm()
        }
    return render(request, 'providers/update_provider.html',context=context)
        
        #Mostramos el formulario con los errores

class ProviderUpdateView(UpdateView):
    model = Provider
    template_name = 'providers/update_provider.html'
    fields = '__all__'
    success_url = '/providers/providers-list/'

def providers_delete(request,pk): #provider.delete()
    provider = Provider.objects.get(id=pk)
    if request.method == 'POST':
        provider.delete()

    return render(request, 'providers/delete_provider.html',context={})


# class ProviderDeleteView(DeleteView):
#     model = Provider
#     template_name = 'providers/delete_provider.html'
#     success_url = '/providers/providers-list/'