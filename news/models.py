from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre 
    

class Publicacion(models.Model):
    # id_publicacion = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    comentario = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario 
