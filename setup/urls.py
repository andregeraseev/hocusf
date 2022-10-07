from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario.views import cadastro, login, logout, dashboard,password_reset_request, upload_comprovante
from show.views import home, lista, listaevento,comprovante, adicionar_nome_lista_com_cadastro, adicionar_nome_lista, index, evento, hocus, dashboard_sem_cadastro
from django.contrib.auth import views as auth_views
admin.site.site_title = 'HOCUS'
admin.site.site_header = 'HOCUS POCUS ADMIN'
admin.site.index_title = 'Administração Shows'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('hocus', hocus, name='hocus'),
    path('lista', lista, name='lista'),
    path('listaevento', listaevento, name='listaevento'),
    path('lista/<int:id>', lista, name='lista'),
    # path('registronomelista', adicionar_nome_lista, name='adicionar_nome_lista'),
    path('adicionar_nome_lista_com_cadastro', adicionar_nome_lista_com_cadastro, name='adicionar_nome_lista_com_cadastro'),
    path('evento/<int:id>', evento, name='evento'),

    path('pagamento', dashboard_sem_cadastro, name='dashboard_sem_cadastro'),


    path('registronomelista/<int:id>', adicionar_nome_lista, name='adicionar_nome_lista'),
    path('comprovante', comprovante, name='comprovante'),
    path('comprovante/<int:id>', comprovante, name='comprovante'),
    path('dashboard', dashboard, name='dashboard'),
    path('upload_comprovante', upload_comprovante, name='upload_comprovante'),
    path('index', index, name='index'),
    path("password_reset", password_reset_request, name="password_reset"),
    # path('accounts/', include('django.contrib.auth.urls'))
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='senhas/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="senhas/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='senhas/password_reset_complete.html'), name='password_reset_complete'),



]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)