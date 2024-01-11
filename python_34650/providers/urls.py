from django.urls import path
from providers.views import providers_list,providers_create,providers_update


urlpatterns = [
    path('providers-list/',providers_list,name='providers_list'),
    path('create-provider/',providers_create,name='providers_create'),
    path('update-provider/<int:id>/',providers_update,name='providers_update'),
]