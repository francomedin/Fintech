from apps.cliente.views import (
    ClienteCreateView,
    ClienteDeleteView,
    ClienteDetailView,
    ClienteUpdateView,
    ClienteListView,
)
from django.urls import path

app_name = 'cliente_app'

urlpatterns = [
    path(
        'cliente/create',
        ClienteCreateView.as_view(),
        name='cliente_create'
    ),

    path(
        'cliente/list',
        ClienteListView.as_view(),
        name='cliente_list'
    ),

    path(
        'cliente/update/<pk>/',
        ClienteUpdateView.as_view(),
        name='cliente_update'
    ),

    path(
        'cliente/detail/<pk>/',
        ClienteDetailView.as_view(),
        name='cliente_detail'
    ),

    path(
        'cliente/delete/<pk>/',
        ClienteDeleteView.as_view(),
        name='cliente_delete'
    ),

]
