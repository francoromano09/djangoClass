from django.urls import path
from providers.views import providers_list, providers_create, providers_update,providers_delete, \
    ProvidersListView, ProviderCreateView,ProviderUpdateView#ProviderDeleteView,


urlpatterns = [
    path('providers-list/',ProvidersListView.as_view(),name='providers_list'),
    path('create-provider/',ProviderCreateView.as_view(),name='providers_create'),
    path('update-provider/<int:pk>/',providers_update,name='providers_update'),
    path('delete-provider/<int:pk>/',providers_delete,name='providers_delete'),
]