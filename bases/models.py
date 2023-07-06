from django.db import models
# importo la tabla user que viene con django para registrar el usuario que trabaja con una clave foranea
from django.contrib.auth.models import User

# Create your models here.


class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    # uto_now_add=True significa que cuando el registro se cree toma la fecha del servidor
    fc = models.DateTimeField(auto_now_add=True)
    # fecha de modif, cada vez que se realice una accion necesito que se modifique para eso uso auto_now=True
    fm = models.DateTimeField(auto_now=True)
    # uc usuario que crea
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # el que modifica no lo puedo referenciar a la misma tabla user
    um = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True  # es para decirle a django que no cree la tabla ya que este modelo va a ser parte de todas las tablas
