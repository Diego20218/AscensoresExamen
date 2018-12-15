from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class registrocliente(models.Model):
   NombreCliente = models.CharField(max_length=40)
   DireccionCliente  = models.CharField(max_length=60)
   CiudadCliente = models.CharField(max_length=60)
   ComunaCliente = models.CharField(max_length=60)
   TelefonoCliente = models.CharField(max_length=9)
   CorreoCliente = models.CharField(max_length=40)
   AsignadoCliente = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null = True)
   Estadosdelcliente = (('Atendido','Atendido'),('No Atendido','No Atendido'),('Terminado','Terminado'),('Cancelado','Cancelado'))
   EstadoCliente = models.CharField(max_length=40,choices=Estadosdelcliente,default='Atendido')

def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()


class PerfilUsuario(models.Model):
    Imagen = models.FileField(upload_to="projects")
    Nombre = models.CharField(max_length = 50)   
    Fecha = models.DateField()
    Edad = models.IntegerField()
    Direccion = models.CharField(max_length = 50)
    Email = models.EmailField()
    Telefono = models.CharField(max_length=8)
    Usuario = models.OneToOneField(User,on_delete=models.CASCADE,unique = True)

class registroascensor(models.Model):
   NombreCliente = models.CharField(max_length=40)
   FechaInicio  = models.DateField()
   HoraInicio = models.CharField(max_length=5)
   HoraTermino = models.CharField(max_length=5)
   ModeloAscensor = models.CharField(max_length=70)
   FallasAscensor = models.CharField(max_length=70)
   ReparacionesEfectuadas = models.CharField(max_length=70)
   PiezasCambiadas = models.CharField(max_length=70)
   NombreTrabajadorAsignado = models.CharField(max_length=40)




