from django.db import models
from django.utils.html import mark_safe
from usuario.models import Usuario, UsuarioSemRegistro


# Model para adicionar usuario na lista de entrada e pagamento, podendo adicionar comprovante


# model para controle dos shows com acesso ao Banner
class Show(models.Model):

    titulo_show = models.CharField(max_length=100, )
    descricao_show = models.CharField(max_length=300)
    horario_do_show = models.CharField(max_length=100, null=True)
    data_do_show = models.DateField(null=True)
    banner = models.ImageField(upload_to='static/banners', blank=True)
    quadrado = models.ImageField(upload_to='static/banners', blank=True)
    ticket = models.ImageField(upload_to='static/ticket', blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null= True )
    publicada = models.BooleanField(default=False)
    pix = models.BooleanField(default=False)
    carrocel = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo_show

    @property
    def banner_preview(self):
        if self.banner:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.banner.url))
        return ""

    @property
    def quadrado_preview(self):
        if self.quadrado:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.quadrado.url))
        return ""

    @property
    def ticket_preview(self):
        if self.ticket:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.ticket.url))
        return ""

class NomeLista(models.Model):
    sem_registro = models.ForeignKey(UsuarioSemRegistro, on_delete=models.CASCADE, blank=True, null= True)
    roqueiro = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null= True)
    pagamento = models.BooleanField(default=False)
    comprovante = models.ImageField(upload_to='static/comprovantes', blank=True)
    lista_reserva = models.ForeignKey(Show, on_delete=models.CASCADE, blank=True, null= True,)

    class Meta:
        unique_together = ('roqueiro', 'lista_reserva')


    def __str__(self):
        return str(self.roqueiro)



