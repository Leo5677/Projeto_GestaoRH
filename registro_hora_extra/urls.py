from django.urls import path
from .views import HoraExtraListView, HoraExtraUpdateView, HoraExtraDeleteView, HoraExtraCreateView

urlpatterns = [
    path('', HoraExtraListView.as_view(), name='list_hora_extra'),
    path('criar/', HoraExtraCreateView.as_view(), name='create_hora_extra'),
    path('deletar/<int:pk>/', HoraExtraDeleteView.as_view(), name='delete_hora_extra'),
    path('editar/<int:pk>/', HoraExtraUpdateView.as_view(), name='update_hora_extra')
]
