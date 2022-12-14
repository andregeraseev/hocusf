from django.contrib import admin
from .models import Show, NomeLista


class ListandoShows(admin.ModelAdmin):
    list_display = ('id', 'titulo_show', 'horario_do_show', 'data_do_show',
                    'publicada', 'habilitar_link', 'link_ingreco', 'pix',  'chave_pix', 'valor','created_at')
    list_display_links = ('id', 'titulo_show', )
    list_editable = ('horario_do_show', 'data_do_show', 'habilitar_link', 'link_ingreco', 'publicada', 'pix', 'chave_pix', 'valor',)
    readonly_fields = ('banner_preview', 'quadrado_preview',)
    def banner_preview(self, obj):
        return obj.banner_preview

    banner_preview.short_description = 'banner_preview'
    banner_preview.allow_tags = True

    def quadrado_preview(self, obj):
        return obj.quadrado_preview

    quadrado_preview.short_description = 'quadrado_preview'
    quadrado_preview.allow_tags = True






admin.site.register(Show, ListandoShows)


class ListandoNomeLista(admin.ModelAdmin):
    list_display = ('id', 'roqueiro', 'sem_registro', 'lista_reserva')
    list_display_links = ('id', 'roqueiro')
    list_filter = ( 'lista_reserva', 'roqueiro')
    search_fields = ['sem_registro__usuario_sem_registro', 'roqueiro__usuario__username' ,]

admin.site.register(NomeLista, ListandoNomeLista)
