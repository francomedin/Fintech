from apps.pago.views import (
    PagoCreateView,
    PagoDeleteView,
    PagoDetailView,
    PagoUpdateView,
    PagoListView,
    PagoPkCreateView
)
from django.urls import path

app_name = 'pago_app'

urlpatterns = [

    #Create
    path(
        'pago/create',
        PagoCreateView.as_view(),
        name='pago_create'
    ),
    #Create_pk
    path(
        'pago/create/<pk>/',
        PagoPkCreateView.as_view(),
        name='pago_create_pk'
    ),
    #List
    path(
        'pago/list/<pk>/',
        PagoListView.as_view(),
        name='pago_list_pk'
    ),
    #Update
    path(
        'pago/update/<pk>/',
        PagoUpdateView.as_view(),
        name='pago_update'
    ),
    #Detail
    path(
        'pago/detail/<pk>/',
        PagoDetailView.as_view(),
        name='pago_detail'
    ),
    #Delete
    path(
        'pago/delete/<pk>/',
        PagoDeleteView.as_view(),
        name='pago_delete'
    ),

]
