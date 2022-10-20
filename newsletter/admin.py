from django.contrib import admin
from newsletter.models import Newsletter

def send_newsletter(modeladmin, request, queryset):


    for newsletter in queryset:
        newsletter.send(request)
        send_newsletter.short_description = "Enviar newsletter para todos os instritos"

class NewsletterList(admin.ModelAdmin):
    list_display = ('id', 'corpo_show', 'mensagem_extra', 'created_at', 'updated_at')
    list_display_links = ('id', )
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterList)
