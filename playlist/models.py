from django.db import models
from django.core.validators import FileExtensionValidator
class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return f"{self.titulo}"

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    filmes = models.ManyToManyField(Musica) 

    def __str__(self):
        return self.nome

# Create your models here.
