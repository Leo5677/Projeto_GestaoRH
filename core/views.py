from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registro_hora_extra.models import RegistroHoraExtra
from rest_framework import viewsets
from core.serializers import *


# Create your views here.

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    funcionarios = request.user.funcionario
    data['total_funcionarios'] = funcionarios.empresas.total_funcionarios
    data['total_funcionarios_ferias'] = funcionarios.empresas.total_funcionarios_ferias
    data['total_funcionarios_doc_pendentes'] = funcionarios.empresas.total_funcionarios_doc_pendentes

    data['total_funcionarios_doc_ok'] = funcionarios.empresas.total_funcionarios_doc_ok
    data['total_funcionarios_rg'] = 10

    data['total_hora_extra_utilizadas'] = RegistroHoraExtra.objects.filter(
        funcionarios__empresas=funcionarios.empresas, utilizada=True).aggregate(Sum('horas'))['horas__sum'] or 0
    data['total_hora_extra_pendente'] = RegistroHoraExtra.objects.filter(
        funcionarios__empresas=funcionarios.empresas, utilizada=False).aggregate(Sum('horas'))['horas__sum'] or 0

    return render(request, 'core/index.html', data)


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerilizer
