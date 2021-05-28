from django.db import models
from django.urls import reverse


# Create your models here.


class Empresa(models.Model):
    nome = models.CharField('Nome Da Empresa', max_length=100)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')
