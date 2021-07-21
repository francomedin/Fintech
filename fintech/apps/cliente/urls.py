from django.urls import path

app_name = 'cliente_app'

urlpatterns = [
    path('cliente/create', ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/list', ClienteList.as_view(), name='cliente_list'),
    path('cliente/update', ClienteUpdate.as_view(), name='cliente_update'),
    path('cliente/detail', ClienteDetail.as_view(), name='cliente_detail'),
    path('cliente/delete', ClienteDelete.as_view(), name='cliente_delete'),

]
