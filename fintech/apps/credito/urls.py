from django.urls import path

app_name = 'credito_app'

urlpatterns = [
    path('credito/create', CreditoCreate.as_view(), name='credito_create'),
    path('credito/list', CreditoList.as_view(), name='credito_list'),
    path('credito/update', CreditoUpdate.as_view(), name='credito_update'),
    path('credito/detail', CreditoDetail.as_view(), name='credito_detail'),
    path('credito/delete', CreditoDelete.as_view(), name='credito_delete'),

]
