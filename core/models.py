from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify
import uuid

#renomeando as imagens
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
        abstract=True

class Projetos(Base):
    titulo = models.CharField('Título', max_length=100)
    comentario = models.TextField('Comentário')
    urlgit = models.URLField('URL GitHub')
    urlsite = models.URLField('URL Site')
    dataConclusao = models.DateField('Data Conclusão')
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': (450, 225)})
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
    