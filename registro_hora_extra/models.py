from django.db import models
from django.urls import reverse

from funcionarios.models import Funcionario


# Create your models here.


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)
    funcionarios = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo

    def get_absolute_url(self):
        return reverse('update_hora_extra', args=[self.id])
