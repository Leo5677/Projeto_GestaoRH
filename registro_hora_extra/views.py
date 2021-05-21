from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm

# Create your views here.


class HoraExtraListView(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        return RegistroHoraExtra.objects.filter(funcionarios__empresas=empresa_logada)


class HoraExtraCreateView(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraUpdateView(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionarios', 'horas']


class HoraExtraDeleteView(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')
