from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())
    
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'Nome: {nome}\nEmail: {email}\nMensagem: {mensagem}'
        
        mail = EmailMessage(
            subject=nome,
            body=conteudo,
            from_email='contato@gui.com.br',
            to=['contato@gui.com.br'],
            headers={'Replay': email},
        )
        mail.send()
