from django.db import models
from usuario.models import Usuario
from show.models import Show

class NomeLista(models.Model):
    pessoa = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    cpf = Usuario.cpf



