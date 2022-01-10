from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Embarque(models.Model):
    status = models.CharField(max_length=15)
    proveedor = models.CharField(max_length=100)
    ctr = models.IntegerField()
    producto = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    um = models.CharField(max_length=20)
    categoria = models.CharField(max_length=15)
    carga = models.CharField(max_length=30)
    tipo = models.CharField(max_length=20)
    eta = models.CharField(max_length=20)
    retiro = models.CharField(max_length=20)
    hora = models.CharField(max_length=20)
    siglaCtr = models.CharField(max_length=30)

    # Si se elimina un 'autor' de un embarque, se elimina sus embarques asociados.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.status