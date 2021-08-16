from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Pago
from django.urls import reverse_lazy
# Create your views here.


class PagoCreateView(CreateView):
    model = Pago
    template_name = 'pago/pago_create.html'
    fields = ('__all__')


class PagoDeleteView(DeleteView):
    template_name = 'pago/pago_delete.html'
    model = Pago
    success_url = reverse_lazy('pago_app:pago_list')


class PagoDetailView(DetailView):
    model = Pago
    template_name = 'pago/pago_detail.html'


class PagoUpdateView(UpdateView):
    template_name = 'pago/pago_update.html'
    model = Pago
    fields = ('__all__')


class PagoListView(ListView):
    model = Pago
    template_name = 'pago/pago_list.html'
    # Poner Paginacion
    context_object_name = 'pagos'