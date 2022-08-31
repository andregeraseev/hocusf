from django.contrib import admin
from usuario.models import Usuario


class ListandoUsuario(admin.ModelAdmin):

    list_display = ('id','usuario', 'cpf', 'celular')
    list_display_links = ('id', 'usuario',)
    list_editable = ('celular',)


admin.site.register(Usuario, ListandoUsuario)
