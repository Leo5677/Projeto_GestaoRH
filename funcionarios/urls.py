from django.urls import path, include
from .views import (
    FuncionariosListView,
    FuncionarioUpdateView,
    FuncionarioDeleteView,
    FuncionarioCreateView,
    Pdf
)
from .views import relatorio_funcionarios

urlpatterns = [
    path('', FuncionariosListView.as_view(), name='list_funcionarios'),
    path('criar/', FuncionarioCreateView.as_view(), name='create_funcionario'),
    path('editar/<int:pk>', FuncionarioUpdateView.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>', FuncionarioDeleteView.as_view(), name='delete_funcionario'),
    path('relatorio_funcionarios/', relatorio_funcionarios, name='relatorio_funcionarios'),
    path('relatorio_funcionarios_html/', Pdf.as_view(), name='relatorio_funcionarios_html'),
]
