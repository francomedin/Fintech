from django.urls import path

from apps.credito.views import (
    CreditoCreateView,
    CreditoListView,
    CreditoUpdateView,
    CreditoDeleteView,
    CreditoDetailView,
    CreditoPkCreate
)

app_name = 'credito_app'

urlpatterns = [
    path(
        'credito/create',
        CreditoCreateView.as_view(),
        name='credito_create'
    ),
    # Crear credito con pk de cliente
    path(
        'credito/create/<pk>/',
        CreditoPkCreate.as_view(),
        name='credito_create_pk'
    ),

    # Listado de creditos filtrados por cliente
    path(
        'credito/list/<pk>/',
        CreditoListView.as_view(),
        name='credito_list'
    ),

    path(
        'credito/update/<pk>/',
        CreditoUpdateView.as_view(),
        name='credito_update'
    ),

    path(
        'credito/detail/<pk>/',
        CreditoDetailView.as_view(),
        name='credito_detail'
    ),

    path(
        'credito/delete',
        CreditoDeleteView.as_view(),
        name='credito_delete'
    ),

]
