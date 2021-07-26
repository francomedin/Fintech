from typing import List
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Cliente
from django.urls import reverse_lazy
# Create your views here.


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente/cliente_create.html'
    fields = ('__all__')


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_app:cliente_list')


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ('__all__')


class ClienteListView(ListView):
    model = Cliente
    # Poner Paginacion
    context_object_name = 'clientes'
