from django.urls import path, include
from .views import DocumentoCreateView

urlpatterns = [
    path('criar/<int:funcionarios_id>/', DocumentoCreateView.as_view(), name='create_documento'),
]
