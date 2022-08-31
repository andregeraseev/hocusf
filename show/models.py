from django.db import models
from django.db import models
from django.utils.html import mark_safe


class Show(models.Model):
    titulo_show = models.CharField(max_length=100)
    descricao_show = models.CharField(max_length=300)
    horario_do_show = models.CharField(max_length=100, null=True)
    data_do_show = models.DateField(null=True)

    def __str__(self):
        return self.titulo_show



class Banner(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    foto_banner = models.ImageField(upload_to='static/banners', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    @property
    def banner_preview(self):
        if self.foto_banner:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.foto_banner.url))
        return ""