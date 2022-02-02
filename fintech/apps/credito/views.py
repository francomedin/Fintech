from django.views.generic.edit import CreateView, FormView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Credito, Cuota
from apps.cliente.models import Cliente
from django.urls import reverse, reverse_lazy
from .forms import CreditoForm, CreditoPkForm
# Create your views here.


class CreditoPkCreate(FormView):

    # Creacion de credito con la pk del cliente seteada

    template_name = 'credito/credito_create.html'
    form_class = CreditoPkForm

    def get_success_url(self):
        return reverse_lazy(
            'credito_app:credito_list',
            kwargs={'pk': self.kwargs['pk']}
        )

    def form_valid(self, form):

        palabra_clave = self.kwargs['pk']
        titular = Cliente.objects.get(pk=palabra_clave)
        capital = form.cleaned_data['capital']
        tasa_interes = form.cleaned_data['tasa_interes']/100
        cant_cuota = form.cleaned_data['cant_cuota']
        fecha = form.cleaned_data['fecha_prestamo']

        credito_obj = Credito.objects.create_credito(
            titular,
            capital,
            fecha,
            tasa_interes,
            cant_cuota
        )
        Cuota.objects.create_cuotas(
            credito_obj,
            capital,
            fecha,
            tasa_interes,
            cant_cuota
        )

        return super(CreditoPkCreate, self).form_valid(form)


class CreditoCreateView(FormView):

    template_name = 'credito/credito_create.html'
    form_class = CreditoForm
    success_url = '/'

    def form_valid(self, form):

        titular = form.cleaned_data['titular']
        capital = form.cleaned_data['capital']
        tasa_interes = form.cleaned_data['tasa_interes']/100
        cant_cuota = form.cleaned_data['cant_cuota']
        fecha = form.cleaned_data['fecha_prestamo']

        credito_obj = Credito.objects.create_credito(
            titular,
            capital,
            fecha,
            tasa_interes,
            cant_cuota
        )
        Cuota.objects.create_cuotas(
            credito_obj,
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

    template_name = 'credito/credito_list.html'

    context_object_name = 'creditos'
    paginate_by = 10
    ordering = 'fecha_prestamo'

    def get_queryset(self):
        palabra_clave = self.kwargs['pk']

        lista = Credito.objects.filter(
            titular=palabra_clave).order_by('-fecha_prestamo')
        return lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        palabra_clave = self.kwargs['pk']
        titular = Cliente.objects.filter(pk=palabra_clave)
        context["titular"] = titular[0]
        return context


class CuotaListView(ListView):
    model = Cuota
    template_name = 'credito/cuota_list.html'
    context_object_name = 'cuotas'

    def get_queryset(self):
        palabra_clave = self.kwargs['pk']
        lista = Cuota.objects.filter(
            credito=palabra_clave).order_by('numero_cuota')
        return lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        palabra_clave = self.kwargs['pk']
        credito = Credito.objects.get(pk=palabra_clave)
        context["credito"] = credito
        return context
