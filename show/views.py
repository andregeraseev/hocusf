from django.shortcuts import render
from django.shortcuts import render
from .models import Banner

def home(request):
    banner = Banner.objects.filter(publicada=True)


    dados = {'banners': banner}

    return render(request, 'home.html', dados)