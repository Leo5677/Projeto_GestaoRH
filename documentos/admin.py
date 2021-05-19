from django.contrib import admin
from .models import Documento

# Register your models here.


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['descricao']