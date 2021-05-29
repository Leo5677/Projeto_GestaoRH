from django.urls import path, include
from .views import home
from rest_framework.routers import SimpleRouter
from .serializers import *
from .views import *

router = SimpleRouter()
router.register('horas-extras', RegistroHoraExtraViewSet)
router.register('funcionarios', FuncionarioViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('drf/', include(router.urls))
]