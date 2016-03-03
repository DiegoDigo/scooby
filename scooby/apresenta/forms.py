from django import forms
from django.core.mail import send_mail
from django.conf import settings

class CadastroForm(forms.Form):
    nome  = forms.CharField(label="Nome",help_text="Email2 ex : email@email.com",max_length='100',widget=forms.TextInput(attrs={'placeholder': 'Nome completo'}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'ex email@Email.com'}))
    msg = forms.CharField(label="Mensagem",widget=forms.Textarea(attrs={'placeholder': 'Mensagem de 255 caracteres '}))

    def send_mail(self):
        subject = "Contato Scooby"
        mensagem = 'Nome %(nome)s \n E-mail %(email)s \n Mensagem %(msg)s'
        context = {
            'nome':self.cleaned_data['nome'],
            'email':self.cleaned_data['email'],
            'msg':self.cleaned_data['msg'],
        }
        mensagem = mensagem % context
        send_mail(subject,mensagem,settings.DEFAULT_FROM_EMAIL,[settings.CONTACT_EMAIL],fail_silently=False)
