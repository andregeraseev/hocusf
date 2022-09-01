from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import cadastro, login, logout
from show.views import home, lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('lista', lista, name='lista'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)