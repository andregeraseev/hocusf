from django.contrib import admin
from .models import Show, NomeLista


class ListandoShows(admin.ModelAdmin):
    list_display = ('id', 'titulo_show', 'descricao_show', 'horario_do_show', 'data_do_show',
                    'publicada', 'pix', 'carrocel')
    list_display_links = ('id', 'titulo_show', )
    list_editable = ('horario_do_show', 'data_do_show', 'publicada', 'pix', 'carrocel',)

    def banner_preview(self, obj):
        return obj.banner_preview

    banner_preview.short_description = 'banner_preview'
    banner_preview.allow_tags = True


admin.site.register(Show, ListandoShows)


class ListandoNomeLista(admin.ModelAdmin):
    list_display = ('id', 'roqueiro', 'sem_registro')
    list_display_links = ('id', 'roqueiro',)


admin.site.register(NomeLista, ListandoNomeLista)
