from django.urls import path, include
from .views import (
    # DocumentosListView,
    # DocumentoUpdateView,
    # DocumentoDeleteView,
    DocumentoCreateView
)

urlpatterns = [
    # path('', DocumentosListView.as_view(), name='list_documento'),
    path('criar/<int:funcionarios_id>/', DocumentoCreateView.as_view(), name='create_documento'),
    # path('editar/<int:pk>', DocumentoUpdateView.as_view(), name='update_documento'),
    # path('deletar/<int:pk>', DocumentoDeleteView.as_view(), name='delete_documento'),
]
