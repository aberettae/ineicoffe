from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.http.response import JsonResponse
# Create your views here.


class DemoView(TemplateView):
    template_name = 'demo/demo.html'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        print(request.GET.get('prueba'))
        return super(DemoView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DemoView, self).get_context_data(**kwargs)
        context.update({
            "nombre": 'Jose',
            "apellido": 'Tello',
            "trabajo": {
                "nombre": 'inei',
                "area": 'otin'
            }
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse({"status": 200})

