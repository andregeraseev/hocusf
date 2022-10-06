from django import forms
from .models import NomeLista

class NomeListaForm(forms.ModelForm):
    class Meta:
        model = NomeLista
        fields = ('comprovante',)

class ContactForm(forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField()
    assunto = forms.CharField()
    mensagem = forms.CharField(widget=forms.Textarea)