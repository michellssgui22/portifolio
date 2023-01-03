from django.views.generic import FormView, TemplateView
from .models import Projetos, Academico, Certificados, VideoApresentacao, ContatoEmail
from .forms import ContatoForm
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs)
        context['principais'] = Projetos.objects.order_by('peso').all()
        context['projetos'] = Projetos.objects.order_by('dataConclusao').all().reverse
        context['academicos'] = Academico.objects.all()
        context['certificados'] = Certificados.objects.order_by('dataConclusao').all().reverse
        context['urls'] = VideoApresentacao.objects.all().values
        return context
    
    def form_valid(self, form, *args, **kwargs):
        form.send_mail() 
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.success(self.request, 'Mensagem  não enviada!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
    

class ProjetosView(TemplateView):
    template_name = 'projetos.html'
    
    def get_context_data(self, **kwargs): 
        context = super(ProjetosView, self).get_context_data(**kwargs)
        context['projetos'] = Projetos.objects.order_by('?').all()
        return context
    
    
class ModalView(TemplateView):
    template_name = 'modal.html'
    

class CurriculoView(TemplateView):
    template_name = 'curriculo.html'
    
    