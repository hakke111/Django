from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    desccripcion = models.TextField()
    caracteristicas = models.TextField()
    precio = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")