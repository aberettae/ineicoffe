from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from .forms import ContactoForm
# Create your views here.


class ContactoView(FormView):
    template_name = 'contactenos/formulario_contactenos.html'
    form_class = ContactoForm
    success_url = reverse_lazy('contactenos:gracias')

    def form_valid(self, form):
        form.save()
        return super(ContactoView, self).form_valid(form)


class AgradecimientoView(TemplateView):
    template_name = 'contactenos/gracias.html'
