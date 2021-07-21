from django.urls import path

app_name = 'pago_app'

urlpatterns = [
    path('pago/create', PagoCreate.as_view(), name='pago_create'),
    path('pago/list', PagoList.as_view(), name='pago_list'),
    path('pago/update', PagoUpdate.as_view(), name='pago_update'),
    path('pago/detail', PagoDetail.as_view(), name='pago_detail'),
    path('pago/delete', PagoDelete.as_view(), name='pago_delete'),

]
