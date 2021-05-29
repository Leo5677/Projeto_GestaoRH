from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from registro_hora_extra.models import *
from rest_framework import viewsets
from core.serializers import *


# Create your views here.

@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'core/index.html', data)


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerilizer
