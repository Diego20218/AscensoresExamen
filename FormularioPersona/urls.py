from django.conf.urls import include, url
from django.urls import path
from . import views
from FormularioPersona.views import RegistroUsuario, VerPerfil, InfoPerfil,VerGeneral, VerListaClientes, Usuario_Edit, VerListaClientesAsignados, RealizarOrden, VerAscensores

app_name = 'hola';
urlpatterns = [
	url(r'^$',  views.pagina_login, name='pagina_login'),
	url(r'^registrar/', RegistroUsuario.as_view(), name='pagina_registrar'),
    url(r'^mostrarperfil/$', VerPerfil, name='VerPerfil'),
    url(r'^crearperfil/$', InfoPerfil, name='InfoPerfil'),
	url(r'^intro/', VerGeneral, name='intro'),
	url(r'^introlistaclientes/$', VerListaClientes, name='introlista'),
	path('introcambiarusuario/<int:id>' ,Usuario_Edit, name='introcambiarusuario'),
	url(r'^misclientesasignados/$', VerListaClientesAsignados, name='misclientesasignados'),
	path('seleccioncliente/<int:id>' ,RealizarOrden, name='seleccionclientes'),
	url(r'^listadeascensorestotal/$', VerAscensores, name='listadeascensorestotal'),
]

