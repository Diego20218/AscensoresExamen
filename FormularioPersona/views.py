from django.shortcuts import render
from django.utils import timezone
from . models import registrocliente
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from FormularioPersona.forms import RegistroForm
from django.views.generic import CreateView
from FormularioPersona.forms import PerfilUser, RegistrarAlCliente, RegistrarAlAscensor
from FormularioPersona.models import PerfilUsuario,registrocliente, User, registroascensor
from django.template import RequestContext
from django.shortcuts import redirect

def pagina_login(request):
	return render(request,'PaginaDelMisPerris/login.html')


class RegistroUsuario(CreateView):
	model = User
	template_name = "PaginaDelMisPerris/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')



def InfoPerfil(request):
	context_instance= RequestContext(request)
	if request.method=='POST':
		Usuario = request.user
		form = PerfilUser(request.POST, request.FILES)
		if form.is_valid():
			Usuario = Usuario
			Imagen = form.cleaned_data['Imagen'] 
			Nombre = form.cleaned_data['Nombre']
			Fecha = form.cleaned_data['Fecha']
			Edad = form.cleaned_data['Edad']
			Direccion = form.cleaned_data['Direccion']
			Email = form.cleaned_data['Email']
			Telefono = form.cleaned_data['Telefono']
			PerfilUsuario.objects.create(Usuario=Usuario, Imagen=Imagen, Nombre=Nombre, Fecha=Fecha, Edad=Edad, Telefono=Telefono,Email=Email,Direccion=Direccion)
			return redirect('hola:VerPerfil')
	else:
		form = PerfilUser()
		return render(request, 'PaginaDelMisPerris/crearperfil.html', {'form':form})

def VerPerfil(request):
	Usuario = request.user
	info = PerfilUsuario.objects.filter(Usuario_id=Usuario.id)
	contexto = {'Info': info}
	return render(request, 'PaginaDelMisPerris/mostrarperfil.html', contexto)



def VerGeneral(request):
	if request.method=='POST':
		form = registrocliente()
		form.NombreCliente = request.POST['NombreCliente']
		form.DireccionCliente = request.POST['DireccionCliente']
		form.CiudadCliente = request.POST['CiudadCliente']
		form.ComunaCliente = request.POST['ComunaCliente']
		form.TelefonoCliente = request.POST['TelefonoCliente']
		form.CorreoCliente = request.POST['CorreoCliente']
		form.save()
	Usuario = request.user
	info = PerfilUsuario.objects.filter(Usuario_id=Usuario.id)
	contexto = {'Info': info}
	return render(request, 'PaginaDelMisPerris/intro.html', contexto)


def VerListaClientes(request):
	Usuario = request.user
	info = PerfilUsuario.objects.filter(Usuario_id=Usuario.id)
	FormularioPersona = registrocliente.objects.all()
	FormularioUsu = User.objects.all()
	contexto = {'Info': info,'ListaClientes':FormularioPersona,'ListaUsuarioUno':FormularioUsu}
	return render(request, 'PaginaDelMisPerris/introlistaclientes.html', contexto)


def Usuario_Edit(request, id):
	bicicleta = registrocliente.objects.get(id = id)
	if request.method == 'GET':
		form = RegistrarAlCliente(instance=bicicleta)
	else:
		form = RegistrarAlCliente(request.POST, instance=bicicleta)
		if form.is_valid():
			form.save()
		return redirect('hola:intro')
	return render(request, 'PaginaDelMisPerris/introlistaclientesasignar.html',{'form': form})



def VerListaClientesAsignados(request):
	Usuario = request.user
	info = PerfilUsuario.objects.filter(Usuario_id=Usuario.id)
	FormularioPersona = registrocliente.objects.filter(AsignadoCliente=Usuario.id)
	contexto = {'Info': info,'ListaClientes':FormularioPersona}
	return render(request, 'PaginaDelMisPerris/intromisclientes.html', contexto)


def RealizarOrden(request, id):
	cliente = registrocliente.objects.get(id = id)
	trabajador = request.user
	if request.method == 'GET':
		form = RegistrarAlAscensor(instance=cliente)
	else:
		form = RegistrarAlAscensor(request.POST, instance=cliente)
		if form.is_valid():
			NombreCliente = form.cleaned_data['NombreCliente']
			FechaInicio = form.cleaned_data['FechaInicio']
			HoraInicio = form.cleaned_data['HoraInicio']
			HoraTermino = form.cleaned_data['HoraTermino']
			ModeloAscensor = form.cleaned_data['ModeloAscensor']
			FallasAscensor = form.cleaned_data['FallasAscensor']
			ReparacionesEfectuadas = form.cleaned_data['ReparacionesEfectuadas']
			PiezasCambiadas = form.cleaned_data['PiezasCambiadas']
			NombreTrabajadorAsignado = trabajador
			registroascensor.objects.create(NombreCliente=NombreCliente,FechaInicio=FechaInicio,HoraInicio=HoraInicio,HoraTermino=HoraTermino,ModeloAscensor=ModeloAscensor,FallasAscensor=FallasAscensor,ReparacionesEfectuadas=ReparacionesEfectuadas,PiezasCambiadas=PiezasCambiadas,NombreTrabajadorAsignado=trabajador)
			form.save()
		return redirect('hola:misclientesasignados')
	return render(request, 'PaginaDelMisPerris/introlistaclientesseleccionar.html',{'form': form})

def VerAscensores(request):
	Usuario = request.user
	info = PerfilUsuario.objects.filter(Usuario_id=Usuario.id)
	FormularioPersona = registroascensor.objects.all()
	contexto = {'Info': info,'ListaAscensores':FormularioPersona}
	return render(request, 'PaginaDelMisPerris/listadeascensorestotal.html', contexto)




