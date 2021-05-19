from django.contrib import admin
from .models import RegistroHoraExtra


# Register your models here.

@admin.register(RegistroHoraExtra)
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ['motivo']
