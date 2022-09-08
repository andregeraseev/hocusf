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
             'show': show,

    }

    return render(request, 'listaevento.html', dados)

def lista(request, id=1):
    # medodo para confimar pagamento e voltar para pagina atual
    if request.method == 'POST':
        id = request.POST['id']
        show = request.POST['show']
        cofirmapagamento = NomeLista.objects.filter(id=id)
        cofirmapagamento.update(
            pagamento=True)

        print(show)
        return redirect('lista/'+show)
    # metodo para rendelizar pagina com lista de pessoas com nome na lista e pix
    else:
        banner = Banner.objects.filter(publicada=True)
        show = Show.objects.filter(id=id)

        dados = {'banners': banner,
                 'show': show
        }

        return render(request, 'lista.html', dados)

def registronomelista(request, id):

    # render pagina registro nome lista
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


def comprovante(request, id):
    # metodo render para comprovante

    banner = Banner.objects.all()
    show = NomeLista.objects.filter(id=id)

    dados = {'banners': banner,
             'show': show
             }

    return render(request, 'comprovante.html', dados)

# def pagamento(request):
#
#     if request.method == 'POST':
#
#         id = request.POST['id']
#         cofirmapagamento = NomeLista.objects.filter(id=id)
#         cofirmapagamento.update(
#             pagamento=True)
#
#         cofirmapagamento.save()



def adicionar_nome_lista(request):
    # metodo para adicoonar nome na lista sem registro
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        celular = request.POST['celular']
        show = request.POST['show']

        # id_show = Show.objects.filter(id=show)
        # print("show a por nome na lista", id_show,)
        # id_cpf = NomeLista.objects.filter(cpf=cpf)
        # print("cpf a por no show", id_cpf )
        # print("CPF JA CADASTRADO")

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
    # adionarnar mensagens de erro