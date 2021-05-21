from django.db import models
from django.urls import reverse
from empresas.models import Empresa

# Create your models here.


class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    empresas = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_departamentos')