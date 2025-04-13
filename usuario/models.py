from django.db import models

# Create your models here.
from django.conf import settings
#crear modelo para fecha de cumpleaños de cada usuario  que se guardara en usuario_profile, ahora cada usuario al registrase tendra su perfil CADA USUARIO donde podra editar SU LASTNAME Y FIRSNAME Y EDITAR O AÑADIR SU CUMPLE ACADA USUARIO 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    informacion_adicional = models.TextField()

    def __str__(self):
        return self.nombre


class RespuestaAutomatica(models.Model):
    pregunta = models.TextField()
    respuesta = models.TextField()

    def __str__(self):
        return self.pregunta


class Interaccion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)