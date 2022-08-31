from django.contrib import admin
from .models import NomeLista


class ListandoNomeLista(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'show', 'cpf')
    list_display_links = ('id', 'show', 'pessoa',)



admin.site.register(NomeLista, ListandoNomeLista)

