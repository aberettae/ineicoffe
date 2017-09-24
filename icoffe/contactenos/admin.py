from django.contrib import admin
from .models import Contacto
# Register your models here.

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'primer_nombre', 'apellido_paterno', 'asunto')

    readonly_fields = ('primer_nombre', 'segundo_nombre', 'apellido_paterno',
                       'apellido_materno', 'asunto', 'contenido', 'tipo')
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


