from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Funcionario
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

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


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Realtório De Funcionários.')

    funcionarios = Funcionario.objects.filter(empresas=request.user.funcionario.empresas)

    str = 'Nome: %s | Hora Extra: %f'

    p.drawString(0, 800, '_' * 150)

    y = 750

    for funcionario in funcionarios:
        p.drawString(10, y, str % (funcionario.nome, funcionario.total_hora_extra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:

    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)

        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):
    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')