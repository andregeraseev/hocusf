from show.models import Show
from usuario.models import Usuario
from django.db import models
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib import messages


class Newsletter(models.Model):
    corpo_show = models.ForeignKey(Show, on_delete=models.CASCADE, blank=True, null= True,)
    # newsletter_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null= True,)
    mensagem_extra = models.TextField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):

        subscribers = Usuario.objects.filter(permicao_newslleters=True)
        show = self.corpo_show
        mensagem = self.mensagem_extra
        counter = 1
        for sub in subscribers:
            from_email = "ageraseev@gmail.com"
            to_emails = sub.usuario.email
            subject = self.subject

            c = {
                'mensagem' : mensagem,
                'show' : show,
                'sub': sub,
                'domain': '127.0.0.1:8000',
                'site_name': 'Website',
                'protocol': 'http',
            }


            lala = render_to_string('email/newsletter.html', c)
            # principal = render_to_string( contents, c )
            message = lala
            # sg.send(message)
            try:
                send_mail(subject, message, from_email, [to_emails], html_message=lala)
                messages.success(request, f' enviado {counter} de {len(subscribers)} Emails, enviado para {to_emails}.')
                counter += 1
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

        messages.success(request, f' Todos Emails enviados.')