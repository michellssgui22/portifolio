from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ProjetosView(TemplateView):
    template_name = 'projetos.html'
    
class ModalView(TemplateView):
    template_name = 'modal.html'
    
