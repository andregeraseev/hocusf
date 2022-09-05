from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import cadastro, login, logout, dashboard
from show.views import home, lista, adicionar_nome_lista, listaevento,registronomelista,comprovante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('lista', lista, name='lista'),
    path('listaevento', listaevento, name='listaevento'),
    path('lista/<int:id>', lista, name='lista'),
    path('adicionar_nome_lista', adicionar_nome_lista, name='adicionar_nome_lista'),
    path('registronomelista/<int:id>', registronomelista, name='registronomelista'),
    path('comprovante', comprovante, name='comprovante'),
    path('comprovante/<int:id>', comprovante, name='comprovante'),
    path('dashboard', dashboard, name='dashboard'),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)