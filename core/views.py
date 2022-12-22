from django.views.generic import TemplateView
from .models import Projetos, Academico, Certificados

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs)
        context['principais'] = Projetos.objects.all()
        context['projetos'] = Projetos.objects.order_by('peso').all()
        context['academicos'] = Academico.objects.all()
        context['certificados'] = Certificados.objects.order_by('dataConclusao').all().reverse
        return context

class ProjetosView(TemplateView):
    template_name = 'projetos.html'
    
    def get_context_data(self, **kwargs): 
        context = super(ProjetosView, self).get_context_data(**kwargs)
        context['projetos'] = Projetos.objects.order_by('?').all()
        return context
    
class ModalView(TemplateView):
    template_name = 'modal.html'
    
