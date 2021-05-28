from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from departamentos.models import Departamento
from empresas.models import Empresa


# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresas = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

    @property
    def total_hora_extra(self):
        false = self.registrohoraextra_set.filter(utilizada=False)
        if false:
            return false.aggregate(Sum('horas'))['horas__sum'] or 0
        else:
            return false or 0

    def get_absolute_url(self):
        return reverse('list_funcionarios')
