from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Credito
from django.urls import reverse_lazy
# Create your views here.


class CreditoCreateView(CreateView):
    model = Credito
    template_name = 'credito/credito_create.html'
    fields = ('__all__')


class CreditoDeleteView(DeleteView):
    template_name = 'credito/credito_delete.html'
    model = Credito
    success_url = reverse_lazy('credito_app:credito_list')


class CreditoDetailView(DetailView):
    model = Credito
    template_name = 'credito/credito_detail.html'


class CreditoUpdateView(UpdateView):
    template_name = 'credito/credito_update.html'
    model = Credito
    fields = ('__all__')


class CreditoListView(ListView):
    model = Credito
    template_name = 'credito/credito_list.html'
    # Poner Paginacion
    context_object_name = 'creditos'
