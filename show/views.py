from django.shortcuts import render
from django.shortcuts import render
from .models import Banner, Show
from usuario.models import Usuario
from nomelista.models import NomeLista

def home(request):

    pessoas= Usuario.objects.all()
    banner = Banner.objects.filter(publicada=True)
    show = Show.objects.all()

    dados = {'banners': banner,
             'show': show,
             'pessoa': pessoas
    }

    return render(request, 'home.html', dados)

def lista(request):


    banner = Banner.objects.filter(publicada=True)
    show = Show.objects.all()

    dados = {'banners': banner,
             'show': show
    }

    return render(request, 'lista.html', dados)