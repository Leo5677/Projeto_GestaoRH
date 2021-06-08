from django.db import models

# Create your models here.


class Teste(models.Model):
    descricao = models.TextField(max_length=255)