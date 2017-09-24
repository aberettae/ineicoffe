from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactoForm
# Create your views here.


class ContactoView(FormView):
    template_name = 'contactenos/formulario_contactenos.html'
    form_class = ContactoForm