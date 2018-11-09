from django import forms

from .models import Vehiculo

class PostForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ('author','marca','modelo','anio','color','numero_puertas','descripcion','precio')