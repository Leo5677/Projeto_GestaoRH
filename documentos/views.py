from django.shortcuts import render
from django.views.generic import *
from .models import Documento


# Create your views here.


class DocumentoCreateView(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionarios_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
