from django.shortcuts import render, redirect
from .models import Show, NomeLista
from usuario.models import Usuario
from django.contrib import messages
from django.db import IntegrityError
from usuario.models import UsuarioSemRegistro
from validate_docbr import CPF
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
# email
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from show.form import ContactForm
import random
dominio = '127.0.0.1:8000'

# def index(request):
#     data_hora = datetime.now()
#     mes = data_hora.strftime('%m')
#     showmes = Show.objects.filter(data_do_show__month=mes, publicada=True)
#     semana = data_hora.strftime('%V')
#     showsemana = Show.objects.filter(data_do_show__week=semana, publicada=True)
#     pessoas = Usuario.objects.all()
#     show = Show.objects.filter(publicada=True)
#     proximos_eventos = Show.objects.filter(publicada=True)
#     dados = {
#         'showdasemana': showsemana,
#         'showdomes': showmes,
#         'shows': show,
#         'pessoa': pessoas,
#         'proximos': proximos_eventos
#     }
#
#     return render(request, 'index.html', dados)


def home(request):
    # contesto
    testdate = datetime.now()
    mes_atual = testdate.month
    ano_atual = testdate.year
    dia_atual = testdate.day
    weekofmonth = (testdate.day + 7 - 1) / 7
    data_hora = datetime(ano_atual, mes_atual, 1)
    print("weekofmonth", dia_atual, mes_atual, ano_atual, data_hora)
    mes = data_hora.strftime('%m')
    ano = data_hora.strftime('%Y')
    showmes = Show.objects.filter(data_do_show__month=mes, publicada=True)
    showano = Show.objects.filter(data_do_show__year=ano, publicada=True)
    semana = testdate.strftime('%V')
    semana_1 = data_hora.strftime('%V')
    semana_2 = int(data_hora.strftime('%V')) + 1
    semana_3 = int(data_hora.strftime('%V')) + 2
    semana_4 = int(data_hora.strftime('%V')) + 3
    semana_5 = int(data_hora.strftime('%V')) + 4

    showsemana = Show.objects.filter(data_do_show__week=semana, publicada=True).order_by('data_do_show')
    showsemana1 = Show.objects.filter(data_do_show__week=semana_1, publicada=True).order_by('data_do_show')
    showsemana2 = Show.objects.filter(data_do_show__week=semana_2, publicada=True).order_by('data_do_show')
    showsemana3 = Show.objects.filter(data_do_show__week=semana_3, publicada=True).order_by('data_do_show')
    showsemana4 = Show.objects.filter(data_do_show__week=semana_4, publicada=True).order_by('data_do_show')
    showsemana5 = Show.objects.filter(data_do_show__week=semana_5, publicada=True).order_by('data_do_show')

    showsdoano = Show.objects.filter(data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_1 = Show.objects.filter(data_do_show__month=1, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_2 = Show.objects.filter(data_do_show__month=2, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_3 = Show.objects.filter(data_do_show__month=3, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_4 = Show.objects.filter(data_do_show__month=4, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_5 = Show.objects.filter(data_do_show__month=5, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_6 = Show.objects.filter(data_do_show__month=6, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_7 = Show.objects.filter(data_do_show__month=7, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_8 = Show.objects.filter(data_do_show__month=8, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_9 = Show.objects.filter(data_do_show__month=9, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_10 = Show.objects.filter(data_do_show__month=10, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_11 = Show.objects.filter(data_do_show__month=11, data_do_show__year=ano, publicada=True).order_by('data_do_show')
    show_mes_12 = Show.objects.filter(data_do_show__month=12, data_do_show__year=ano, publicada=True).order_by('data_do_show')


    pessoas = Usuario.objects.all()
    show = Show.objects.filter(publicada=True).order_by('-data_do_show')
    proximos_eventos = Show.objects.filter(publicada=True)

    dados = {

        'show_mes_1': show_mes_1,
        'show_mes_2': show_mes_2,
        'show_mes_3': show_mes_3,
        'show_mes_4': show_mes_4,
        'show_mes_5': show_mes_5,
        'show_mes_6': show_mes_6,
        'show_mes_7': show_mes_7,
        'show_mes_8': show_mes_8,
        'show_mes_9': show_mes_9,
        'show_mes_10': show_mes_10,
        'show_mes_11': show_mes_11,
        'show_mes_12': show_mes_12,
        'showdasemana5': showsemana5,
        'showdasemana4': showsemana4,
        'showdasemana3': showsemana3,
        'showdasemana2': showsemana2,
        'showdasemana1': showsemana1,
        'showdasemana': showsemana,
        'showdomes': showmes,
        'shows': show,
        'pessoa': pessoas,
        'proximos': proximos_eventos
    }

    # para contatos via email
    if request.method == 'POST' and 'email_s' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["assunto"]
            from_email = form.cleaned_data["email"]
            message = form.cleaned_data['mensagem']
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            mensagem = "nome: " + nome + '\n' + "email: " + from_email + '\n' + "telefone :" + telefone + '\n' + message
            try:
                send_mail(subject, mensagem, from_email, ["xflavors@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return render(request, 'index.html',
                          {'showdasemana5': showsemana5,
                            'showdasemana4': showsemana4,
                            'showdasemana3': showsemana3,
                            'showdasemana2': showsemana2,
                            'showdasemana1': showsemana1,
                            'showdasemana': showsemana,
                            'showdomes': showmes,
                            'shows': show,
                            'pessoa': pessoas,
                            'proximos': proximos_eventos,
                            'nome': nome,
                            'action': 'recebemos seu email',
                            'form': ContactForm(request.POST)})

    else:
        # HOME
        return render(request, 'index.html', dados)


def hocus(request):
    return render(request, 'hocus.html')


def listaevento(request):
    # lista de shows cadastrados publicados apenas para autorizados
    if request.user.is_staff:
        roqueiros = NomeLista.objects.all()
        show = Show.objects.filter(publicada=True)
        dados = {
            'roqueiro': roqueiros,
            'show': show,
        }

        return render(request, 'listaevento.html', dados)
    else:
        return redirect('home')


def lista(request, id):
    # medodo para confimar pagamento e voltar para pagina atual
    if request.user.is_staff:

        if request.method == 'POST' and 'entrou' in request.POST:
            print(request.POST)
            id_nome_lista = request.POST['id']

            confirma_pagamento_entrada = NomeLista.objects.filter(id=id_nome_lista)
            if confirma_pagamento_entrada.filter(entrou='False'):

                confirma_pagamento_entrada.update(
                    entrou=True)
            else:
                confirma_pagamento_entrada.update(
                    entrou=False)

            pessoa = NomeLista.objects.filter(lista_reserva_id=id)
            show = Show.objects.filter(id=id)
            dados = {'pessoas': pessoa,
                     'show': show
                     }
            return render(request, 'lista.html', dados)

        elif request.method == 'POST':
            print("lista POST")
            id_nome_lista = request.POST['id']
            show = request.POST['show']
            cofirmapagamento = NomeLista.objects.filter(id=id_nome_lista)

            cofirmapagamento.update(
                pagamento=True)
            print(cofirmapagamento, "confima pagamento")

            pagando = id_nome_lista
            # print(cofirmapagamento, "confima pagamento id")
            email_confirma_pagamento(pagando)

            pessoa = NomeLista.objects.filter(lista_reserva_id=id)
            show = Show.objects.filter(id=id)
            dados = {'pessoas': pessoa,
                     'show': show
                     }

            return render(request, 'lista.html', dados)
        # metodo para rendelizar pagina com lista de pessoas com nome na lista e pix
        else:
            print("lista GET")
            pessoa = NomeLista.objects.filter(lista_reserva_id=id)
            show = Show.objects.filter(id=id)
            print(pessoa, "Pessoa")
            dados = {'pessoas': pessoa,
                     'show': show
                     }

            return render(request, 'lista.html', dados)

    else:
        return redirect('home')


# def registronomelista(request, id):
#     show = Show.objects.filter(id=id)
#     dados = {
#
#         'show': show
#     }
#     print(request)
#     return render(request, 'registrarnomelista.html', dados)


# def nomelista(request):
#
#     pessoas= Usuario.objects.all()
#     show = Show.objects.all(publicada=True)
#
#     dados = {
#              'show': show,
#              'pessoa': pessoas
#     }
#
#     return render(request, 'registrarnomelista.html', dados)


def comprovante(request, id):
    # metodo render para comprovante

    if request.method == 'POST':
        # print('AQUIIIIII')
        show = NomeLista.objects.filter(id=id)
        # print(show, "SHOWWWW")
        dados = {
            'show': show
        }

        id_nome_lista = request.POST['id']
        # print(id_nome_lista, "ID_NOME_LISTA")
        # show = request.POST['show']
        cofirmapagamento = NomeLista.objects.filter(id=id_nome_lista)
        # print(cofirmapagamento," CONFIRMA PAGAMENTO")
        cofirmapagamento.update(
            pagamento=True)


        pagando = id_nome_lista
        # print(cofirmapagamento, "confima pagamento id")
        email_confirma_pagamento(pagando)




        return render(request, 'comprovante.html', dados)
    else:

        show = NomeLista.objects.filter(id=id)
        dados = {
            'show': show
        }

        return render(request, 'comprovante.html', dados)




def email_confirma_pagamento(pagando):
    # print(pagando, "Numero do nome lista")
    nomelista_atual = NomeLista.objects.get(pk=pagando)
    # print(nomelista_atual.lista_reserva, "nome do show")
    show = nomelista_atual.lista_reserva
    if nomelista_atual.roqueiro:
        emailusuario = nomelista_atual.roqueiro.usuario.email
        usuario = nomelista_atual.roqueiro.usuario
    else:
        emailusuario = nomelista_atual.sem_registro.email_sem_registro
        usuario = nomelista_atual.sem_registro.usuario_sem_registro

    # associated_users = nomelista_atual.roqueiro.usuario

    subject = f"O pagamento do evento {show} foi aprovado."
    email_html = "email/pagamento_confirmado.html."
    email_template_name = "email/confimacao_nome_lista.txt"
    c = {
        "nome_lista" : nomelista_atual,
        "email": emailusuario,
        # precisa mudar na producao
        'domain': dominio,
        "show": show,
        "usuario": usuario,
        'site_name': 'Website',
        "user": nomelista_atual.roqueiro,
        'protocol': 'http',
    }
    html_message = render_to_string(email_html, c)
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, 'admin@example.com', [emailusuario], html_message=html_message, fail_silently=False)

    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect("home")


def evento(request, id):
    show = Show.objects.filter(id=id)
    dados = {

        'show': show
    }
    print(request)
    return render(request, 'evento.html', dados)


def adicionar_nome_lista(request, id):
    # metodo para adicoonar nome na lista sem cadastro
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        celular = request.POST['celular']
        shows = request.POST['show']
        email_sem_registro = request.POST["email_sem_registro"]
        senha_unica = random_digits()
        show = Show.objects.filter(id=id)

        context = {
            'show': show,
            'form': request.POST}
        print(request, "<<<<request" "Metodo POST adionando nome na lista")
        if not validacpf(cpf):
            messages.warning(request, 'CPF invalido', "danger")
            return render(request, 'registrarnomelista.html', context)
        else:
            showcompleto = Show.objects.get(id=shows)
            try:
                user_sem_registro = UsuarioSemRegistro.objects.create(

                    usuario_sem_registro=nome,
                    cpf_sem_registro=cpf,
                    celular_sem_registro=celular,
                    email_sem_registro = email_sem_registro,
                    senha_unica = senha_unica
                )

                registrando = NomeLista.objects.create(
                    sem_registro=user_sem_registro,
                    lista_reserva=showcompleto
                )
                registrando.save()
                messages.success(request, 'Verefique seu email para confimar seu nome na lista')

                # return redirect('home')

                user_sem_registro.save()

                # EMAIL
                registro = registrando.id
                email_sem_nome_lista(registro)

                return redirect('home')

            except IntegrityError:
                messages.warning(request,
                                 'Tivemos algum probleme para por seu nome na lista, por gentileza entre em contato')
                return redirect('home')

    else:
        print(request, "<<<<request" "Metodo Get adionando nome na lista")
        show = Show.objects.filter(id=id)
        dados = {

            'show': show
        }

        return render(request, 'registrarnomelista.html', dados)
    # adionarnar mensagens de erro

def dashboard_sem_cadastro(request):
    sub = NomeLista.objects.get(id=request.GET['id'])
    if sub.sem_registro.senha_unica == request.GET['senha_unica']:

        usuario = sub.sem_registro.id

        print(usuario)
        show = NomeLista.objects.filter(sem_registro=usuario)

        dados = {
            'eventos': show
        }

        return render(request, 'comprovante_sem_cadastro.html', dados)
    else:
        return redirect('home')

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
            # messages.success(request, 'Seu nome foi colocado na lista com sucesso')
            # return redirect('home')

            # EMAIL
            id_nomelista = user_com_registro.id
            email_nomelista(id_nomelista)
            messages.success(request, 'Seu nome foi colocado na lista com sucesso')
            return redirect('home')


        except IntegrityError:
            messages.warning(request,
                             'Seu nome já está nesse show. Acesse "Meus Eventos" no menu superior para ver mais informações.')
            return redirect('home')

    else:
        return render(request, 'home.html')


def email_nomelista(id_nomelista):
    # print(id_nomelista, "Numero do nome lista")
    nomelista_atual = NomeLista.objects.get(pk=id_nomelista)
    # print(nomelista_atual.lista_reserva, "nome do show")
    show = nomelista_atual.lista_reserva
    emailusuario = nomelista_atual.roqueiro.usuario.email
    usuario = nomelista_atual.roqueiro.usuario
    associated_users = nomelista_atual.roqueiro.usuario

    subject = "Confirmação do Show"
    email_html = "email/confimacao_nome_lista.html"
    email_template_name = "email/confimacao_nome_lista.txt"
    c = {
        "email": emailusuario,
        # precisa mudar na producao
        'domain': dominio,
        "show": show,
        "usuario": usuario,
        'site_name': 'Website',
        "user": nomelista_atual.roqueiro,
        'protocol': 'http',
    }
    html_message = render_to_string(email_html, c)
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, 'admin@example.com', [emailusuario], html_message=html_message, fail_silently=False)

    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect("home")



def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)

def email_sem_nome_lista(registro):
    print(registro, "Numero do nome lista")
    nomelista_atual = NomeLista.objects.get(pk=registro)
    print(nomelista_atual.lista_reserva, "nome do show")
    show = nomelista_atual.lista_reserva
    emailusuario = nomelista_atual.sem_registro.email_sem_registro
    usuario = nomelista_atual.sem_registro.usuario_sem_registro
    # associated_users = nomelista_atual.roqueiro.usuario

    subject = "Confirmação do evento " + str(show)
    email_template_name = "email/dashboard_sem_registro.txt"
    email_html = "email/dashboard_sem_registro.html"
    c = {
        "id": registro,
        "chave": nomelista_atual.sem_registro.senha_unica,
        "email": emailusuario,
        # precisa mudar na producao
        'domain': dominio,
        "show": show,
        "usuario": usuario,
        'site_name': 'Website',
        "user": nomelista_atual.roqueiro,
        'protocol': 'http',
    }
    html_message = render_to_string(email_html, c)
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, 'admin@example.com', [emailusuario], html_message=html_message, fail_silently=False)

    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect("home")



def validacpf(cpf):
    validacao = CPF().validate(cpf)
    return validacao
