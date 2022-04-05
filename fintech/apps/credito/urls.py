from django.urls import path,re_path

from apps.credito.views import (
    CreditoCreateView,
    CreditoListView,
    CreditoUpdateView,
    CreditoDeleteView,
    CreditoDetailView,
    CreditoPkCreate,
    CuotaListView,
    MoraCreatePk,
    MoraListPk,
    MoraDeleteView,
    MoraUpdateView,
    MoraDetailView,
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
        'credito/delete/<pk>/',
        CreditoDeleteView.as_view(),
        name='credito_delete'
    ),

    path(
        'cuota/list/<pk>/',
        CuotaListView.as_view(),
        name='cuota_list'
    ),

    path(
        'credito/cuota/mora/<pk>/',
        MoraCreatePk.as_view(),
        name='mora_create'
    ),
#-------------------------Mora Urls
    path(
        'credito/cuota/mora/<pk>/',
        MoraCreatePk.as_view(),
        name='mora_create'
    ),
    path(
        'credito/mora/list/<pk>/',
        MoraListPk.as_view(),
        name='mora_list_pk'
    ),
    path(
        'credito/mora/delete/<pk>/',
        MoraDeleteView.as_view(),
        name='mora_delete'
    ),
    path(
        'credito/mora/update/<pk>/',
        MoraUpdateView.as_view(),
        name='mora_update'
    ),
    path(
        'mora/detail/<pk>/',
        MoraDetailView.as_view(),
        name='mora_detail'
    ),

]
