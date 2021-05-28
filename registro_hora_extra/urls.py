from django.urls import path
from .views import (
    HoraExtraListView,
    HoraExtraUpdateView,
    HoraExtraBaseUpdateView,
    HoraExtraDeleteView,
    HoraExtraCreateView,
    UtilizouHoraExtraView,
    NaoUtilizouHoraExtraView,
    ExportarCsv,
    ExportarExcel
)

urlpatterns = [
    path('', HoraExtraListView.as_view(), name='list_hora_extra'),
    path('criar/', HoraExtraCreateView.as_view(), name='create_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDeleteView.as_view(), name='delete_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraUpdateView.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraBaseUpdateView.as_view(), name='update_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/',  UtilizouHoraExtraView.as_view(), name='utilizou_hora_extra_base'),
    path('nao-utilizou-hora-extra/<int:pk>/', NaoUtilizouHoraExtraView.as_view(), name='nao-utilizou_hora_extra_base'),
    path('exportar-csv', ExportarCsv.as_view(), name='exportar_csv'),
    path('exportar-excel', ExportarExcel.as_view(), name='exportar_excel')
]


