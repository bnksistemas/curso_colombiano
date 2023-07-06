from django.db import models
from bases.models import ClaseModelo

# Create your models here.


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100, help_text='Descripción de la categorai', unique=True

    )

    def __str__(self):
        return '{}' .format(self.descripcion)

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural = "Categorias"
        db_table="categoria"
