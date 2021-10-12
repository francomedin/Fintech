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
    # Create url
    path(
        'cliente/create',
        ClienteCreateView.as_view(),
        name='cliente_create'
    ),

    # List url
    path(
        'cliente/list',
        ClienteListView.as_view(),
        name='cliente_list'
    ),

    # Update url
    path(
        'cliente/update/<pk>/',
        ClienteUpdateView.as_view(),
        name='cliente_update'
    ),

    # Detail url
    path(
        'cliente/detail/<pk>/',
        ClienteDetailView.as_view(),
        name='cliente_detail'
    ),

    # Delete url
    path(
        'cliente/delete/<pk>/',
        ClienteDeleteView.as_view(),
        name='cliente_delete'
    ),

]
