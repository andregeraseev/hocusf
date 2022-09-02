from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Banner, Show, NomeLista
from usuario.models import Usuario
from django.contrib import messages

def home(request):

    pessoas= Usuario.objects.all()
    banner = Banner.objects.filter(publicada=True)
    show = Show.objects.all()

    dados = {'banners': banner,
             'show': show,
             'pessoa': pessoas
    }

    return render(request, 'home.html', dados)



def listaevento(request):


    banner = Banner.objects.filter(publicada=True)
    show = Show.objects.all()

    dados = {'banners': banner,
             'show': show
    }

    return render(request, 'listaevento.html', dados)

def lista(request, id):


    banner = Banner.objects.filter(publicada=True)
    show = Show.objects.filter(id=id)

    dados = {'banners': banner,
             'show': show
    }

    return render(request, 'lista.html', dados)

def registronomelista(request, id):


    banner = Banner.objects.filter(id=id)
    show = Show.objects.all()

    dados = {'banners': banner,
             'show': show
    }

    return render(request, 'registrarnomelista.html', dados)


def nomelista(request):

    pessoas= Usuario.objects.all()
    banner = Banner.objects.filter(publicada=True)
    show = Show.objects.all()

    dados = {'banners': banner,
             'show': show,
             'pessoa': pessoas
    }

    return render(request, 'registrarnomelista.html', dados)


def adicionar_nome_lista(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        celular = request.POST['celular']
        show = request.POST['show']
        user_sem_registro = NomeLista.objects.create(
            nome=nome,
            cpf=cpf,
            celular=celular)

        user_sem_registro.save()



        nome_show = Show.objects.get(id=show)

        nome_show.lista_reserva_sr.add(user_sem_registro)


        messages.success(request, 'Seu nome foi colocado na lista com sucesso')
        return redirect('home')

    else:
        return render(request, 'registrarnomelista.html')