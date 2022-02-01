from django.views.generic.edit import FormView, UpdateView
from django.views.generic import ListView, DeleteView
from django.views.generic.detail import DetailView
from .models import Pago
from .forms import PagoForm
from django.urls import reverse_lazy
# Create your views here.


class PagoCreateView(FormView):
    model = Pago
    template_name = 'pago/pago_create.html'
    form_class = PagoForm
    success_url = '/'

    def form_valid(self, form):

        cuota = form.cleaned_data['cuota']
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
        Pago.objects.set_situacion(
            cuota,
            monto,
            fecha
        )
        Pago.objects.set_mora(
            cuota,
            fecha
        )

        return super(PagoCreateView, self).form_valid(form)


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
    paginate_by = 10

    def get_queryset(self):
        palabra_clave = self.kwargs['pk']

        lista = Pago.objects.filter(
            cuota=palabra_clave).order_by('fecha')
        return lista
