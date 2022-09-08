from django.db import models
from django.contrib.auth.models import User
from show.models import Show

class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    celular = models.CharField(max_length=12)

    def __str__(self):
        return str(self.usuario)

