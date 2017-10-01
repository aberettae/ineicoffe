from django.contrib import admin
from .models import Personal
# Register your models here.

@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos')
