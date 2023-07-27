from django.db import models

# Create your models here.
class Autores(models.Model):
    autor = models.CharField(max_length=100)
    contato = models.IntegerField()
    email = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    trabalho = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_entrega = models.DateField()


