from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='id de categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria