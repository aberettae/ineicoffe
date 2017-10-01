from django.shortcuts import render
from django.views.generic import FormView, DetailView
from django.urls import reverse
from .models import Reserva
from .forms import ReservaForm
# Create your views here.


class ReservaView(FormView):
    template_name = 'reservas/reserva.html'
    form_class = ReservaForm

    def form_valid(self, form):
        form.instance.codigo = form.instance.get_codigo_ramdon()
        form.save()

        self.detalle_reserva = form.instance.codigo
        return super(ReservaView, self).form_valid(form)

    def get_success_url(self):
        return reverse('reserva:detalle', kwargs={"pk": self.detalle_reserva})



class DetalleReservaView(DetailView):
    model = Reserva
    template_name = 'reservas/detalle_reserva.html'
