from django.contrib import admin
from .models import NomeLista
from usuario.models import Usuario


@admin.register(NomeLista)
class ListandoNomeLista(admin.ModelAdmin):
    def _cpf(self, obj):
        return Usuario.objects.get(id=obj.id).cpf



    list_display = ('id', '_cpf')
    list_display_links = ('id',)

