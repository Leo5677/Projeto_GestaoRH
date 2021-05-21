from django.urls import path, include
from .views import (
    DepartamentosListView,
    DepartamentoUpdateView,
    DepartamentoDeleteView,
    DepartamentoCreateView
)

urlpatterns = [
    path('', DepartamentosListView.as_view(), name='list_departamentos'),
    path('criar/', DepartamentoCreateView.as_view(), name='create_departamento'),
    path('editar/<int:pk>', DepartamentoUpdateView.as_view(), name='update_departamento'),
    path('deletar/<int:pk>', DepartamentoDeleteView.as_view(), name='delete_departamento'),
]
