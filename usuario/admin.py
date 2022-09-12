from django.contrib import admin
from usuario.models import Usuario, UsuarioSemRegistro


class ListandoUsuario(admin.ModelAdmin):

    list_display = ('id','usuario', 'cpf', 'celular')
    list_display_links = ('id', 'usuario',)
    list_editable = ('celular',)


admin.site.register(Usuario, ListandoUsuario)

class ListandoUsuarioSemRegistro(admin.ModelAdmin):

    list_display = ('id','usuario_sem_registro', 'cpf_sem_registro', 'celular_sem_registro')
    list_display_links = ('id', 'usuario_sem_registro',)
    list_editable = ('celular_sem_registro',)


admin.site.register(UsuarioSemRegistro, ListandoUsuarioSemRegistro)