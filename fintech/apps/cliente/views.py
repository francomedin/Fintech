from typing import List
from django.db.models import fields
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Cliente
from django.urls import reverse_lazy
from .forms import ClienteForm
# Create your views here.


class ClienteCreateView(CreateView):
    form_class = ClienteForm
    template_name = 'cliente/cliente_create.html'

    #success_url = reverse_lazy('cliente_app:cliente_list')

    def get_success_url(self):
        return reverse('cliente_app:cliente_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ClienteCreateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente_app:cliente_list')
    template_name = 'cliente/cliente_delete.html'


class ClienteDetailView(DetailView):
    
    model = Cliente
    template_name = 'cliente/cliente_detail.html'


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm

    template_name = 'cliente/cliente_update.html'

    def get_success_url(self):
        return reverse('cliente_app:cliente_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ClienteUpdateView, self).get_form_kwargs(
            *args, **kwargs)
        return kwargs


class ClienteListView(ListView):
    model = Cliente
    # Poner Paginacion
    context_object_name = 'clientes'
    template_name = 'cliente/cliente_list.html'
