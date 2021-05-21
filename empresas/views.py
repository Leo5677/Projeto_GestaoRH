from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa


# Create your views here.


class EmpresaCreateView(CreateView):
    model = Empresa
    fields = '__all__'

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresas = obj
        funcionario.save()
        return HttpResponse('Ok')


class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = '__all__'

