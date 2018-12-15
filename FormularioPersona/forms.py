from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from FormularioPersona.models import PerfilUsuario, registrocliente, registroascensor

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = {
        'username',
        'first_name',
        'last_name',
        'email',
        }
        labels = {
        'username': 'Nombre de usuario',
        'first_name': 'Nombre',
        'last_name': 'Apellido',
        'email': 'Correo',
        }


class PerfilUser(forms.ModelForm):
    class Meta:
        model = PerfilUsuario

        fields = [
        'Imagen',
        'Nombre',
        'Fecha',
        'Edad',
        'Direccion',
        'Email',
        'Telefono',
        #'Usuario',
        ]

        labels = {
        'Imagen': 'Imagen',
        'Nombre': 'Nombre',
        'Fecha': 'Fecha',
        'Edad' : 'Edad',
        'Direccion': 'Direccion',
        'Email': 'Email',
        'Telefono': 'Telefono',
        #'Usuario': 'Usuario',
        }

        widgets = {
        'Nombre': forms.TextInput(attrs={'class':'form-control'}),
        'Fecha': forms.TextInput(attrs={'class':'form-control','type':'date'}),
        'Edad': forms.TextInput(attrs={'class':'form-control'}),      
        'Direccion': forms.TextInput(attrs={'class':'form-control'}),
        'Email': forms.EmailInput(attrs={'class':'form-control'}),
        'Telefono': forms.TextInput(attrs={'class':'form-control'}),
        #'Usuario': forms.Select(attrs={'class':'form-control'}),
        }

class RegistrarAlCliente(forms.ModelForm):
    class Meta:
        model = registrocliente

        fields = [
        'NombreCliente',
        'DireccionCliente',
        'CiudadCliente',
        'ComunaCliente',
        'TelefonoCliente',
        'CorreoCliente',
        'AsignadoCliente',
        'EstadoCliente',

        #'Usuario',
        ]

        labels = {
        'NombreCliente': 'NombreCliente',
        'DireccionCliente': 'DireccionCliente',
        'CiudadCliente': 'CiudadCliente',
        'ComunaCliente' : 'ComunaCliente',
        'TelefonoCliente': 'TelefonoCliente',
        'CorreoCliente': 'CorreoCliente',
        'AsignadoCliente': 'AsignadoCliente',
        'EstadoCliente': 'EstadoCliente',
        #'Usuario': 'Usuario',
        }

        widgets = {
        'NombreCliente': forms.TextInput(attrs={'class':'form-control'}),
        'DireccionCliente': forms.TextInput(attrs={'class':'form-control'}),
        'CiudadCliente': forms.TextInput(attrs={'class':'form-control'}),
        'ComunaCliente': forms.TextInput(attrs={'class':'form-control'}),
        'TelefonoCliente': forms.TextInput(attrs={'class':'form-control'}),
        'CorreoCliente': forms.EmailInput(attrs={'class':'form-control'}),
        'AsignadoCliente': forms.Select(attrs={'class':'form-control'}),
        'EstadoCliente': forms.Select(attrs={'class':'form-control'}),
        #'Usuario': forms.Select(attrs={'class':'form-control'}),
        }


class RegistrarAlAscensor(forms.ModelForm):
    class Meta:
        model = registroascensor

        fields = [
        'NombreCliente',
        'FechaInicio',
        'HoraInicio',
        'HoraTermino',
        'ModeloAscensor',
        'FallasAscensor',
        'ReparacionesEfectuadas',
        'PiezasCambiadas',


        #'Usuario',
        ]

        labels = {
        'NombreCliente': 'NombreCliente',
        'FechaInicio': 'FechaInicio',
        'HoraInicio': 'HoraInicio',
        'HoraTermino' : 'HoraTermino',
        'ModeloAscensor': 'ModeloAscensor',
        'FallasAscensor': 'FallasAscensor',
        'ReparacionesEfectuadas': 'ReparacionesEfectuadas',
        'PiezasCambiadas': 'PiezasCambiadas',
        
        #'Usuario': 'Usuario',
        }

        widgets = {
        'NombreCliente': forms.TextInput(attrs={'class':'form-control'}),
        'FechaInicio': forms.TextInput(attrs={'class':'form-control','type':'date'}),
        'HoraInicio': forms.TextInput(attrs={'class':'form-control'}),
        'HoraTermino': forms.TextInput(attrs={'class':'form-control'}),
        'ModeloAscensor': forms.TextInput(attrs={'class':'form-control'}),
        'FallasAscensor': forms.TextInput(attrs={'class':'form-control'}),
        'ReparacionesEfectuadas': forms.TextInput(attrs={'class':'form-control'}),
        'PiezasCambiadas': forms.TextInput(attrs={'class':'form-control'}),

        #'Usuario': forms.Select(attrs={'class':'form-control'}),
        }




