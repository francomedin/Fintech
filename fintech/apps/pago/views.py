from django.views.generic.edit import FormView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Pago
from apps.credito.models import Credito, Cuota
from .forms import PagoForm, PagoPkForm
from django.urls import reverse_lazy, reverse
# Create your views here.
from apps.credito.models import Cuota


class PagoCreateView(FormView):
    model = Pago
    template_name = 'pago/pago_create.html'
    form_class = PagoForm
    success_url = '/'

    def form_valid(self, form):

        palabra_clave = self.kwargs['pk']
        cuota = Cuota.objects.get(pk=palabra_clave)
        monto = form.cleaned_data['monto']
        fecha = form.cleaned_data['fecha']
        descripcion = form.cleaned_data['descripcion']
        tipo = form.cleaned_data['tipo']
        metodo = form.cleaned_data['metodo']
        cobrador = form.cleaned_data['cobrador']

        Pago.objects.cargar_pago(
            cuota,
            monto,
            fecha,
            descripcion,
            tipo,
            metodo,
            cobrador

        )
      
       
        return super(PagoCreateView, self).form_valid(form)

    def get_success_url(self):
        pago=Pago.objects.get(pk=self.kwargs['pk'])
        credito_pk=pago.cuota.credito.pk
       
        return reverse_lazy(
            'credito_app:credito_list',
            kwargs={'pk': credito_pk}
        )

class PagoDeleteView(DeleteView):
    template_name = 'pago/pago_delete.html'
    model = Pago
    
    
    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        print(f'pago {self.object}')
        cuota=self.object.cuota
        success_url = self.get_success_url()
        self.object.delete()
        Pago.objects.total_pagado(cuota)
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        cuota_obj=Pago.objects.get(pk=self.kwargs['pk'])
        cuota_pk=cuota_obj.cuota.pk

        return reverse_lazy(
            'pago_app:pago_list_pk',
            kwargs={'pk': cuota_pk}
        )

class PagoDetailView(DetailView):
    model = Pago
    template_name = 'pago/pago_detail.html'


class PagoUpdateView(UpdateView):
    template_name = 'pago/pago_update.html'
    model = Pago
    fields = ('__all__')
    def get_success_url(self):
        cuota_obj=Pago.objects.get(pk=self.kwargs['pk'])
        cuota_pk=cuota_obj.cuota.pk

        return reverse_lazy(
            'pago_app:pago_list_pk',
            kwargs={'pk': cuota_pk}
        )

class PagoListView(ListView):
    model = Pago
    template_name = 'pago/pago_list.html'
    # Poner Paginacion
    context_object_name = 'pagos'
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.kwargs['pk']

        lista = Pago.objects.filter(
            cuota=palabra_clave).order_by('fecha')
        return lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        palabra_clave = self.kwargs['pk']
        cuota = Cuota.objects.get(pk=palabra_clave)
        context["cuota"] = cuota
        return context

# Pk passed as parameter.


class PagoPkCreateView(FormView):

    template_name = 'pago/pago_create.html'
    form_class = PagoPkForm
    success_url = '/'

    def form_valid(self, form):
        palabra_clave = self.kwargs['pk']
        cuota = Cuota.objects.get(pk=palabra_clave)
        monto = form.cleaned_data['monto']
        fecha = form.cleaned_data['fecha']
        descripcion = form.cleaned_data['descripcion']
        tipo = form.cleaned_data['tipo']
        metodo = form.cleaned_data['metodo']
        cobrador = form.cleaned_data['cobrador']

        Pago.objects.cargar_pago(
            cuota,
            monto,
            fecha,
            descripcion,
            tipo,
            metodo,
            cobrador

        )
        Pago.objects.set_situacion(cuota)
      
        return super(PagoPkCreateView, self).form_valid(form)

    def get_success_url(self):
       
        cuota=Cuota.objects.get(pk=self.kwargs['pk'])
        credito_pk=cuota.credito.pk
       
        return reverse_lazy(
            'credito_app:cuota_list',
            kwargs={'pk': credito_pk}
        )