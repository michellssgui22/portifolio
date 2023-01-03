from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
import uuid



# renomeando as imagens
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
# Create your models here.


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    modificado = models.DateField('Modificado', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Projetos(Base):
    titulo = models.CharField('Título', max_length=100)
    comentario = models.TextField('Comentário')
    urlgit = models.URLField('URL GitHub')
    urlsite = models.URLField('URL Site')
    dataConclusao = models.DateField('Data Conclusão')
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': (450, 225)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    peso = models.IntegerField('Peso do Projeto')

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

    def __str__(self):
        return self.titulo


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)


signals.pre_save.connect(produto_pre_save, sender=Projetos)


class Academico(Base):
    instituicao = models.CharField('Instituição', max_length=100)
    formacao = models.CharField('Formação', max_length=200)
    paragrafo1 = models.TextField('Primeiro Praragrafo', max_length=1000)
    paragrafo2 = models.TextField(
        'Segundo Praragrafo', max_length=1000, blank=True)
    paragrafo3 = models.TextField(
        'Terceiro Praragrafo', max_length=1000, blank=True)
    dataInicio = models.DateField('Data Inicio')
    dataFim = models.DateField('Data Fim')

    class Meta:
        verbose_name = 'Academico'
        verbose_name_plural = 'Academicos'

    def __str__(self):
        return self.formacao


class Certificados(Base):
    curso = models.CharField('Título', max_length=100)
    instituicao = models.CharField('Instituição', max_length=100)
    urlvalidacao = models.URLField('URL Validação')
    totalHoras = models.IntegerField('Total Horas')
    dataConclusao = models.DateField('Data Conclusão')
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': (450, 225)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return self.curso


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.curso)


signals.pre_save.connect(produto_pre_save, sender=Certificados)


class VideoApresentacao(Base):
    url = models.URLField('URL')
    data = models.DateField('Data Upload')
    
    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'

    def __str__(self):
        return self.url
    

class ContatoEmail(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    mensagem = models.TextField('Mensagem', max_length=500)
    
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.nome
    
    