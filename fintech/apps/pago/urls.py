from apps.pago.views import (
    PagoCreateView,
    PagoDeleteView,
    PagoDetailView,
    PagoUpdateView,
    PagoListView,
)
from django.urls import path

app_name = 'pago_app'

urlpatterns = [
    
    path(
        'pago/create',
        PagoCreateView.as_view(),
        name='pago_create'
    ),

    path(
        'pago/list/<pk>/',
        PagoListView.as_view(),
        name='pago_list'
    ),

    path(
        'pago/update/<pk>/',
        PagoUpdateView.as_view(),
        name='pago_update'
    ),

    path(
        'pago/detail/<pk>/',
        PagoDetailView.as_view(),
        name='pago_detail'
    ),

    path(
        'pago/delete/<pk>/',
        PagoDeleteView.as_view(),
        name='pago_delete'
    ),

]
