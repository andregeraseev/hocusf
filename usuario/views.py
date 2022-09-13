from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Usuario
from show.models import Show
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



cpf = CPF()



def cadastro(request):

    """Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        cpf = request.POST['cpf']
        celular = request.POST['celular']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not validacpf(cpf):
            messages.error(request, 'CPF invalido')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(cpf):
            messages.error(request, 'O campo CPF não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(celular):
            messages.error(request, 'O campo celular não pode ficar em branco')
            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        if Usuario.objects.filter(cpf=cpf).exists():
            messages.error(request, 'CPF ja cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(
            username=nome,
            email=email,
            password=senha)

        id_usuario = User.objects.get(username=nome)

        perfil = Usuario.objects.create(
            usuario=id_usuario,
            cpf=cpf,
            celular=celular
        )

        user.save()
        perfil.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
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
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('home')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def dashboard(request):
    # mostrando shows com nome na lista e adiconando comprovante
    if request.method == 'POST' and request.FILES['imagem']:

        id = request.POST['id']
        imagem = request.FILES['imagem']
        fss = FileSystemStorage()
        fss.save(imagem.name, imagem)
        recibo = NomeLista.objects.filter(id=id)
        recibo.update(comprovante=imagem)

        if request.user.is_authenticated:
            usuario = request.user.usuario.id
            # cpf = request.user.usuario.cpf
            # # nome = NomeLista.objects.filter(cpf=cpf)
            show = NomeLista.objects.filter(roqueiro_id=usuario)

            dados = {

                'eventos': show
            }

        return render(request, 'dashboard.html', dados)

    else:

        if request.user.is_authenticated:
            usuario = request.user.usuario.id
            # cpf = request.user.usuario.cpf
            # # nome = Usuario.objects.filter(cpf=cpf)
            print(usuario)
            show = NomeLista.objects.filter(roqueiro_id=usuario)
            # 'nome': nome,
            dados = {
                'eventos': show
            }
            return render(request, 'dashboard.html', dados)
        else:
            return redirect('home')


def password_reset_request(request):
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
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="senhas/password_reset.html", context={"password_reset_form":password_reset_form})




def campo_vazio(campo):
    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2

def validacpf(cpf):
    validacao = CPF().validate(cpf)
    return validacao