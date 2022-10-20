from django.contrib import messages, auth
from .models import Usuario
from django.core.exceptions import ValidationError
from show.models import NomeLista
from django.core.files.storage import FileSystemStorage
from validate_docbr import CPF
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
import re
cpf = CPF()
dominio = '127.0.0.1:8000'

def cadastro(request):
    """Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        cpf = request.POST['cpf']
        celular = request.POST['celular']
        check = request.POST.get('check', '') == 'on'
        print(check)
        form= {
            "form": request.POST, }



        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco', "nome")
            return render(request, 'cadastro.html', form)
        if not validacpf(cpf):
            messages.error(request, 'CPF invalido', "cpf")
            return render(request, 'cadastro.html', form)
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco', "email")
            return render(request, 'cadastro.html', form)
        if campo_vazio(cpf):
            messages.error(request, 'O campo CPF não pode ficar em branco', "cpf")
            return render(request, 'cadastro.html', form)
        if campo_vazio(celular):
            messages.error(request, 'O campo celular não pode ficar em branco', "celular")
            return render(request, 'cadastro.html', form)
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais', "senha2")
            return render(request, 'cadastro.html', form)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado', "email")
            return render(request, 'cadastro.html', form)
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF ja cadastrado', "cpf")
            return render(request, 'cadastro.html', form)
        minimal_number = 1
        minimal_upper_char = 1
        minimal_lower_char = 1
        minimal_special_char = 1
        minimal_len_char = 8
        print("teste password")
        if len(senha or ()) < minimal_len_char:
            print("falhou digitos")
            messages.error(request, 'A senha precisa ter no minimo ' + str(minimal_len_char) + ' caracteres',
                           "senha")
            return render(request, 'cadastro.html', form)
        if len(re.findall(r"[A-Z]", senha)) < minimal_upper_char:
            print("falhou maiuscula")
            messages.error(request, 'Senha tem que ter no mínimo ' + str(minimal_upper_char) + ' caracteres maiusculo', "senha")
            return render(request, 'cadastro.html', form)
        if len(re.findall(r"[a-z]", senha)) < minimal_lower_char:
            print("falhou minuscula")
            messages.error(request, 'Senha tem que ter no mínimo ' + str(minimal_lower_char) + ' letras minusculas',
                           "senha")
            return render(request, 'cadastro.html', form)

        if len(re.findall(r"[0-9]", senha)) < minimal_number:
            print("falhou numero")
            messages.error(request, 'Senha tem que ter no mínimo ' + str(minimal_number) + ' numeros', "senha")
            return render(request, 'cadastro.html', form)
        if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", senha)) < minimal_special_char:
            print("falhou carctere especial")
            messages.error(request,
                           'Senha tem que ter no mínimo ' + str(minimal_special_char) + ' caracteres especiais', "senha")
            return render(request, 'cadastro.html', form)

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado', "nome")
            return render(request, 'cadastro.html', form)


        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha)

        id_usuario = User.objects.get(username=nome)

        perfil = Usuario.objects.create(
            usuario=id_usuario,
            cpf=cpf,
            celular=celular,
            permicao_newslleters =check
        )

        user.save()
        perfil.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        # email
        pegando_id_usuario = perfil.id
        print(pegando_id_usuario, "pegando id")
        email_hocus_beta(pegando_id_usuario)

        # fim email
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            # Login pos cadastro

            if user is not None:
                auth.login(request, user)

        return redirect('home')


    else:
        return render(request, 'cadastro.html')




def login(request):
    """Realiza o login de uma pessoa no sistema"""
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.warning(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('home')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)

            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('home')
            # erro senha errada
            else:
                messages.warning(request, 'Verifique sua senha')
                return redirect('home')

        else:
            messages.warning(request, 'Seu email ou sua senha estão incorretos')
            return redirect('home')
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


def upload_comprovante(request):
    # """ area para adicionar comprovante"""
    if request.method == 'POST':

        if not 'imagem' in request.FILES:
            messages.error(request, "Você precisa anexar um comprovante", "danger")
            return redirect("dashboard")

        else:
            imagem = request.FILES['imagem']
            id = request.POST['id']
            imagemsize = imagem.size

            if imagemsize > 5485760:
                messages.warning(request, "Você nao pode enviar uma imagem maior que 5Mb")
                return redirect("dashboard")
            else:

                # form = NomeListaForm(request.POST, request.FILES)
                # if form.is_valid():
                #    form.save()
                #    print("FORMULARIO VALIDO")
                #    recibo = NomeLista.objects.filter(id=id)
                #    recibo.update(comprovante=imagem)
                #    messages.success(request, "Comprovante Adicionado com sucesso")
                #    return redirect("dashboard")




                fss = FileSystemStorage(location="media/comprovantes",
                                        base_url="comprovantes")
                filename = fss.save(imagem.name.replace(" ", "_"), imagem)
                uploaded_file_url = fss.url(filename)
                recibo = NomeLista.objects.filter(id=id)
                recibo.update(comprovante=uploaded_file_url)
                messages.success(request, "Comprovante Adicionado com sucesso")
                print(uploaded_file_url)
                return redirect("dashboard")


def dashboard(request):
    # """mostrando shows com nome na lista e adiconando comprovante"""

    if request.user.is_authenticated:
        usuario = request.user.usuario.id

        print(usuario)
        show = NomeLista.objects.filter(roqueiro_id=usuario)

        dados = {
            'eventos': show
        }
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('home')


def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError("Você nao pode enviar uma imagem maior que 5Mb")
    else:
        return value

def password_reset_request(request):
    #  reset do password por email
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "senhas/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': dominio,
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="senhas/password_reset.html",
                  context={"password_reset_form": password_reset_form})





def email_hocus_beta(pegando_id_usuario):
    id_usuario = Usuario.objects.get(id=pegando_id_usuario)
    print(id_usuario)
    # print(id_nomelista, "Numero do nome lista")
    usuario = Usuario.objects.get(id=pegando_id_usuario)
    print(usuario)
    # print(nomelista_atual.lista_reserva, "nome do show")

    emailusuario = usuario.usuario.email
    print(emailusuario)
    usuario = usuario
    associated_users = usuario

    subject = "Obrigado por participar da hocus beta"
    email_template_name = "email/projetobeta.txt"
    c = {
        "email": emailusuario,
        'domain': dominio,

        "usuario": usuario,
        'site_name': 'Website',
        "user": usuario,
        'protocol': 'http',
    }
    email = render_to_string(email_template_name, c)
    try:
        send_mail(subject, email, 'admin@example.com', [emailusuario], fail_silently=False)

    except BadHeaderError:
        return HttpResponse('Invalid header found.')


def campo_vazio(campo):
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2


def validacpf(cpf):
    validacao = CPF().validate(cpf)
    return validacao

def test_password(senha, request, form):
    minimal_number = 1
    minimal_upper_char = 1
    minimal_lower_char = 1
    minimal_special_char = 1
    minimal_len_char = 8
    print("teste password")
    if len(senha or ()) < minimal_len_char:
        print("falhou digitos")
        messages.error(request, 'A senha precisa ter no minimo 8 digitos' +str(minimal_len_char)+' caracteres', "nome")
        return render(request, 'cadastro.html', form)
    if len(re.findall(r"[A-Z]", senha)) < minimal_upper_char:
        print("falhou maiuscula")
        messages.error(request, 'Senha tem que ter no mínimo '+str(minimal_upper_char)+ ' caracteres', "nome")
        return render(request, 'cadastro.html', form)
    if len(re.findall(r"[a-z]", senha)) < minimal_lower_char:
        print("falhou minuscula")
        messages.error(request,'Senha tem que ter no mínimo '+str(minimal_lower_char)+' letras minusculas', "nome")
        return render(request, 'cadastro.html', form)

    if len(re.findall(r"[0-9]", senha)) < minimal_number:
        print("falhou numero")
        messages.error(request, 'Senha tem que ter no mínimo '+str(minimal_number)+' numeros', "nome")
        return render(request, 'cadastro.html', form)
    if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", senha)) < minimal_special_char:
        print("falhou carctere especial")
        messages.error(request, 'Senha tem que ter no mínimo '+str(minimal_special_char)+' caracteres especiais', "nome")
        return render(request, 'cadastro.html', form)
    else:
        pass


