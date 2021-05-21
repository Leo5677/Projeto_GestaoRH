from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView

from .models import Funcionario


# Create your views here.


class FuncionariosListView(ListView):
    model = Funcionario
    paginate_by = 10

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresas
        return Funcionario.objects.filter(empresas=empresa_logada)


class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresas = self.request.user.funcionario.empresas
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreateView, self).form_valid(form)


class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')
