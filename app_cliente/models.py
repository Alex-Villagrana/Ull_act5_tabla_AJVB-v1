from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)

# Es para el administrador servidor admin
    def __str__(self):
        return f"{self.nombre} {self.edad}"
