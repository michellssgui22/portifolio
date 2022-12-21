from django.contrib import admin
from .models import Projetos

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataConclusao', 'peso', 'modificado', 'ativo' )
