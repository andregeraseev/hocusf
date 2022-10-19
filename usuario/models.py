from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11)
    celular = models.CharField(max_length=12)
    permicao_newslleters = models.BooleanField(default=True)

    def __str__(self):
        return str(self.usuario)


class UsuarioSemRegistro(models.Model):
    usuario_sem_registro = models.CharField(max_length=50)
    cpf_sem_registro = models.CharField(max_length=11)
    celular_sem_registro = models.CharField(max_length=12)
    email_sem_registro = models.EmailField(blank=True, null= True)
    senha_unica = models.CharField(max_length=12, blank=True, null= True)

    def __str__(self):
        return str(self.usuario_sem_registro)
