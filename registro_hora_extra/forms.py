from django.forms import ModelForm
from .models import RegistroHoraExtra
from funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionarios'].queryset = Funcionario.objects.filter(empresas=user.funcionario.empresas)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionarios', 'horas']
