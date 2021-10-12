from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Credito
from django.urls import reverse, reverse_lazy
from .forms import CreditoForm
# Create your views here.


class CreditoCreateView(FormView):

    template_name = 'credito/credito_create.html'
    form_class = CreditoForm
    success_url = '/'

    def form_valid(self, form):

        cuota = 0

        capital = form.cleaned_data['capital']
        tasa_interes = form.cleaned_data['tasa_interes']/100
        cant_cuota = form.cleaned_data['cant_cuota']
        fecha = form.cleaned_data['fecha_prestamo']

        Credito.objects.create_credito(
            capital,
            fecha,
            tasa_interes,
            cant_cuota
        )

        return super(CreditoCreateView, self).form_valid(form)

    


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
