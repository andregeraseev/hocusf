from django.shortcuts import render, redirect
from .models import Show, NomeLista
from usuario.models import Usuario
from django.contrib import messages
from django.db import IntegrityError
from usuario.models import UsuarioSemRegistro
from validate_docbr import CPF


def home(request):

    pessoas= Usuario.objects.all()
    show = Show.objects.filter(publicada=True)

    dados = {
             'shows': show,
             'pessoa': pessoas
    }

    return render(request, 'home.html', dados)


def listaevento(request):

    show = Show.objects.filter(publicada=True)
    dados = {
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
        pessoa = NomeLista.objects.filter(lista_reserva_id=id)
        show = Show.objects.filter(id=id)

        dados = {'pessoas': pessoa,
                 'show': show
        }

        return render(request, 'lista.html', dados)

def registronomelista(request, id):

    show = Show.objects.filter(id=id)
    dados = {
             'show': show
    }

    return render(request, 'registrarnomelista.html', dados)


def nomelista(request):

    pessoas= Usuario.objects.all()
    show = Show.objects.all(publicada=True)

    dados = {
             'show': show,
             'pessoa': pessoas
    }

    return render(request, 'registrarnomelista.html', dados)


def comprovante(request, id):
    # metodo render para comprovante

    show = NomeLista.objects.filter(id=id)
    dados = {
             'show': show
             }

    return render(request, 'comprovante.html', dados)


def adicionar_nome_lista(request):
    # metodo para adicoonar nome na lista sem cadastro
    if request.method == 'POST':
        nome = request.POST['nome']
        # usuarioid = request.POST['usuarioid']
        cpf = request.POST['cpf']
        celular = request.POST['celular']
        show = request.POST['show']


        if not validacpf(cpf):
            messages.warning(request, 'CPF invalido')
            return redirect('registronomelista/' + show)

        showcompleto = Show.objects.get(id=show)

        user_sem_registro = UsuarioSemRegistro.objects.create(

            usuario_sem_registro = nome,
            cpf_sem_registro = cpf,
            celular_sem_registro = celular
            )

        registrando= NomeLista.objects.create(
            sem_registro=user_sem_registro,
            lista_reserva=showcompleto
        )
        registrando.save()
        messages.success(request, 'Seu nome foi colocado na lista com sucesso')
        return redirect('home')

        user_sem_registro.save()

    else:
        return render(request, 'home')
    # adionarnar mensagens de erro

def adicionar_nome_lista_com_cadastro(request):
    # metodo para adicoonar nome na lista com cadastro
    if request.method == 'POST':
        show = request.POST['show']
        usuarioid = request.POST['usuarioid']

        showcompleto = Show.objects.get(id=show)
        usuarioompleto = Usuario.objects.get(id=usuarioid)

        try:
            user_com_registro = NomeLista.objects.create(
                roqueiro=usuarioompleto,
                lista_reserva=showcompleto
                )
            user_com_registro.save()
            messages.success(request, 'Seu nome foi colocado na lista com sucesso')
            return redirect('home')
        except IntegrityError:
            messages.warning(request, 'Seu nome ja esta nesse show')
            return redirect('home')



    else:
        return render(request, 'home.html')
    # adionarnar mensagens de erro


def validacpf(cpf):
    validacao = CPF().validate(cpf)
    return validacao