from django.contrib import admin
from .models import Projetos, Academico, Certificados, VideoApresentacao, ContatoEmail

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataConclusao', 'peso', 'modificado', 'ativo' )
    

@admin.register(Academico)
class AcademicoAdmin(admin.ModelAdmin):
    list_display = ('instituicao', 'formacao', 'dataInicio', 'dataFim', 'modificado', 'ativo')


@admin.register(Certificados)
class CertificadosAdmin(admin.ModelAdmin):
    list_display = ('curso', 'instituicao', 'dataConclusao', 'totalHoras', 'modificado', 'ativo')


@admin.register(VideoApresentacao)
class VideoApresentacaoAdmin(admin.ModelAdmin):
    list_display = ('url', 'modificado', 'ativo')
    

@admin.register(ContatoEmail)
class ContatoEmailAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'mensagem')