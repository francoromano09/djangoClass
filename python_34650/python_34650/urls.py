"""
URL configuration for python_34650 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from python_34650.views import hola_mundo,otra_mas,fecha_actual,vista_con_edad,\
    vista_con_template, saludo_desde_template,index


urlpatterns = [
    path('',index,name='index'),
    path('admin/', admin.site.urls),
    path('hola/', hola_mundo),
    path('otra/', otra_mas),
    path('fecha/', fecha_actual),
    path('edad/<int:edad>', vista_con_edad),
    path('vista-con-template/', vista_con_template),
    path('saludo-desde-template/', saludo_desde_template),

    path('products/', include('products.urls')), # Para poder ordenar las urls de products
]
