from django.shortcuts import render
from .models import NomeLista

def NomeNaLista(request):
    """Listando usuarios e na lista de um show"""

    def get_queryset(self):
        queryset = NomeLista.objects.filter(show_id=self.kwargs['pk'])
        return queryset


