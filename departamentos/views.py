from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Departamento


# Create your views here.


class DepartamentosListView(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logado = self.request.user.funcionario.empresas
        return Departamento.objects.filter(empresas=empresa_logado)


class DepartamentoCreateView(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresas = self.request.user.funcionario.empresas
        departamento.save()
        return super(DepartamentoCreateView, self).form_valid(form)


class DepartamentoUpdateView(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentoDeleteView(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')
