from django.contrib import admin
from .models import registrocliente, PerfilUsuario, registroascensor

admin.site.register(registrocliente)
admin.site.register(registroascensor)
admin.site.register(PerfilUsuario)

# Register your models here.
