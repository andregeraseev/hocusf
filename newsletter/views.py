from django.shortcuts import render
from usuario.models import Usuario

# Create your views here.
def newsletter(request):
    usuario = Usuario
    context = {
        "usuario" : usuario
    }

    if request.method == 'POST':
        usuario_id = request.POST["usuario"]

        tira_news = Usuario.objects.filter(id = usuario_id)
        tira_news.update(permicao_newslleters = False)



        usuario = Usuario
        context = {
            "teste": tira_news,
            "usuario": usuario,
            "usuario_id": usuario_id,
            "alerta": "alerta"
        }
        return render(request, "sair_newsletter.html", context)

    else:
        return render(request, "sair_newsletter.html", context)



