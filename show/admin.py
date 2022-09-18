from django.contrib import admin
from .models import Show, NomeLista


class ListandoShows(admin.ModelAdmin):
    list_display = ('id', 'titulo_show', 'descricao_show', 'horario_do_show', 'data_do_show',
                    'publicada', 'pix', 'carrocel', 'valor')
    list_display_links = ('id', 'titulo_show', )
    list_editable = ('horario_do_show', 'data_do_show', 'publicada', 'pix', 'carrocel', 'valor',)
    readonly_fields = ('banner_preview', 'quadrado_preview', 'ticket_preview',)
    def banner_preview(self, obj):
        return obj.banner_preview

    banner_preview.short_description = 'banner_preview'
    banner_preview.allow_tags = True

    def quadrado_preview(self, obj):
        return obj.quadrado_preview

    quadrado_preview.short_description = 'quadrado_preview'
    quadrado_preview.allow_tags = True

    def ticket_preview(self, obj):
        return obj.ticket_preview

    ticket_preview.short_description = 'ticket_preview'
    ticket_preview.allow_tags = True




admin.site.register(Show, ListandoShows)


class ListandoNomeLista(admin.ModelAdmin):
    list_display = ('id', 'roqueiro', 'sem_registro')
    list_display_links = ('id', 'roqueiro',)


admin.site.register(NomeLista, ListandoNomeLista)
