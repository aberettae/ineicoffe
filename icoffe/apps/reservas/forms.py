from django import forms
from .models import Reserva


class ReservaForm(forms.ModelForm):
    dni = forms.CharField(label='DNI o Pasaporte',max_length=8, min_length=8, required=True,
                          widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese DNI 8 caracteres"}))
    class Meta:
        model = Reserva
        fields = ('nombres', 'apellidos', 'dni', 'nro_personas', 'fecha', 'mesa', 'detalle', )

    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)

        #self.fields['dni'].widget = forms.NumberInput()
        for field in self.fields:
            #print(dir(self.fields[field]))
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })

        self.fields['nombres'].widget.attrs.update({
            "placeholder": "Ingrese un nombre"
        })

        self.fields['nombres'].label = 'Nombre del Titular'

