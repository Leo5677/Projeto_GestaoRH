from django.urls import path
from .views import EmpresaCreateView, EmpresaUpdateView

urlpatterns = [
    path('criar/', EmpresaCreateView.as_view(), name='create_empresa'),
    path('editar/<int:pk>/', EmpresaUpdateView.as_view(), name='edit_empresa')
]
