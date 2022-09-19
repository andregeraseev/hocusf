from django import forms
from .models import NomeLista

class NomeListaForm(forms.ModelForm):
    class Meta:
        model = NomeLista
        fields = ('comprovante',)