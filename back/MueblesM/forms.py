from django import forms
from  .models import  Mueble


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Mueble
        fields = '__all__'

        widget = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

