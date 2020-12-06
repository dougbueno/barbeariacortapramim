from django.db import models

class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    ano = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)
