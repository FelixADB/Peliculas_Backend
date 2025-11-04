from django.db import models

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    popularidad = models.IntegerField(default=0)
    fecha_creacion = models.DateField(auto_now_add=True)
    icono = models.ImageField(upload_to='generos_iconos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=150)
    ano_lanzamiento = models.IntegerField()
    duracion = models.IntegerField(null=True, blank=True, help_text="Duración en minutos")
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='peliculas')

    def __str__(self):
        return self.titulo