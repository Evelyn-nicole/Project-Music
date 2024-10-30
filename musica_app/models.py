from django.db import models

# Create your models here.
class SelloDiscografico(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class PerfilRedesSociales(models.Model):
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()
    
    def __str__(self):
        return f"Instagram: {self.instagram}" 
    
class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    genero_musical = models.CharField(max_length=50)
    perfil = models.OneToOneField(PerfilRedesSociales, on_delete=models.CASCADE)
    sello = models.ForeignKey(SelloDiscografico, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Album(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=50)
    artistas = models.ManyToManyField(Artista)
    
    def __str__(self):
        return self.titulo