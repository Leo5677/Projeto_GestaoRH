from django.db import models
from django.urls import reverse


# Create your models here.


class Empresa(models.Model):
    nome = models.CharField('Nome Da Empresa', max_length=100)

    def __str__(self):
        return self.nome

    @property
    def total_funcionarios(self):
        return self.funcionario_set.all().count()

    @property
    def total_funcionarios_ferias(self):
        return self.funcionario_set.filter(ferias=True).count()

    @property
    def total_funcionarios_doc_pendentes(self):
        return self.funcionario_set.filter(documento=None).count()

    @property
    def total_funcionarios_doc_ok(self):
        from django.db.models import Q
        return self.funcionario_set.filter(~Q(documento=None)).count()


    def get_absolute_url(self):
        return reverse('home')
