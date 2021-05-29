from registro_hora_extra.models import *
from funcionarios.models import *
from rest_framework import serializers


class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = '__all__'


class FuncionarioSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'
