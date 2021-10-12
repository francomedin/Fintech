from django.urls import path
from apps.credito.views import (
    CreditoCreateView,
    CreditoListView,
    CreditoUpdateView,
    CreditoDeleteView,
    CreditoDetailView
)

app_name = 'credito_app'

urlpatterns = [
    path(
        'credito/create',
        CreditoCreateView.as_view(),
        name='credito_create'
    ),

    path(
        'credito/list',
        CreditoListView.as_view(),
        name='credito_list'
    ),

    path(
        'credito/update',
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
