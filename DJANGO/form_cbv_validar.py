

"""
Módulo >>> form_cbv_validar.py
"""

"OBS: (pip install django-bootstrap4) só está sendo utilizado, por eu não saber usar mensagens sem a ferramenta"
def terminal():
    """
    pip install django==2.2.17
    pip install django-bootstrap4
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = [{'DIRS': ['templates']}]
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    """

def forms():
    """
    from django import forms
    from django.core.mail.message import EmailMessage

    class UserOpinionForm(forms.Form):
        name = forms.CharField(label='Seu nome', min_length=2, max_length=100)
        email = forms.EmailField(label='Seu e-mail', min_length=2, max_length=100)
        subject = forms.CharField(label='Assunto', min_length=2, max_length=100)
        message = forms.CharField(label='Sua mensagem', widget=forms.Textarea())

        def print_into_terminal(self):
            content = \
                f'''
                Nome: {self.cleaned_data['name']}
                Email: {self.cleaned_data['email']}
                Assunto: {self.cleaned_data['subject']}
                Mensagem:
                {self.cleaned_data['message']}
                '''

            data_display = EmailMessage(
                body=content,
                headers={'Reply-To': self.cleaned_data['email']},
                subject=self.cleaned_data['subject'],
                to=('meu-email@domínio.com',),
                from_email='meu-email@domínio.com'
            )
            data_display.send()
    """

"OBS: (IndexTemplateView) é usado para servir o formulário (UserOpinionView) no redirecionamento na var (success_url)"
"OBS: messages.success() & messages.error() exibem mensagens caso o formulário seja, ou não, válido"
def views():
    """
    from django.views.generic import TemplateView
    from django.views.generic import FormView
    from .forms import UserOpinionForm
    from django.contrib import messages
    from django.urls import reverse_lazy

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'

    class UserOpinionFormView(FormView):
        template_name = 'form.html'
        form_class = UserOpinionForm
        success_url = reverse_lazy('index')

        def form_valid(self, form, *args, **kwargs):
            form.print_into_terminal()
            messages.success(self.request, 'Sua mensagem foi enviada. Obrigado!')
            return super(UserOpinionFormView, self).form_valid(form, *args, **kwargs)

        def form_invalid(self, form, *args, **kwargs):
            messages.error(self.request, 'Há algum erro no seu formulário!')
            return super(UserOpinionFormView, self).form_invalid(form, *args, **kwargs)
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *
    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('form/', UserOpinionFormView.as_view(), name='form/')
    ]
    """

# index.html
def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
        <style>body {background-color: #222; color: white;}</style>
    </head>
    <body>
        {% bootstrap_messages %}
        <h2>Página inicial</h2>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# form.html
def templates2():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link
            crossorigin="anonymous"
            href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css"
            integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2"
            rel="stylesheet"
        >
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página de formulário</title>
        <style>.ma {margin: auto;}</style>
    </head>
    <body>
        <!--
            Caso seja preciso usar dados de upload, usar atributo abaixo:
                <form enctype="multipart/form-data"></form>

            Caso queira mais segurança em formulário
                <form autocomplete="off"></form>
        -->

        <!--
            Em minha opinião, cada linha de input deve estar configurada da seguinte forma:

                <div class="row">
                    <div class="form-group ma">
                        <input class="form-control">
                    </div>
                </div>

            Em minha opinião, cada linha de input deve ter acessibilidade

                <div class="row">
                    <div class="form-group ma">
                        <label for="nome do campo">Nome do campo</label>
                        <input id="nome do campo">
                    </div>
                </div>
        -->
        <div class="container">
            <form action="{% url 'form/' %}" class="form" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <div class="text-center">
                    <h2>Formulário</h2>
                    <h6>Diga-nos sua opinião</h6>
                </div>
                <div class="row">
                    <div class="form-group ma mt-2">
                        <label class="sr-only" for="name">Campo para informar nome</label>
                        <input class="form-control" id="name" max="100" min="2" name="name" placeholder="seu nome" size="40" type="text" required>
                    </div>
                </div>
                <div class="row">
                    <div class="form-group ma mt-2">
                        <label class="sr-only" for="email">Campo para informar email</label>
                        <input class="form-control" id="email" max="100" min="2" name="email" placeholder="seu e-mail" size="40" type="email" required>
                    </div>
                </div>
                <div class="row">
                    <div class="form-group ma mt-2">
                        <label class="sr-only" for="subject">Campo para informar um assunto</label>
                        <input class="form-control" id="subject" max="100" min="2" name="subject" placeholder="seu assunto" size="40" type="text" required>
                    </div>
                </div>
                <div class="row">
                    <div class="form-group ma mt-2">
                        <label class="sr-only" for="message">Campo para informar mensagem</label>
                        <textarea class="form-control" id="message" name="message" placeholder="escreva a mensagem aqui" rows="7" cols="40" required oninvalid="alert('O campo de mensagem deve ser preenchido!');"></textarea>
                    </div>
                </div>
                <div class="row">
                    <div class="ma mt-5">
                        <button class="btn btn-dark" form="this-form" type="submit">Enviar mensagem</button>
                    </div>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def terminal2():
    """
    python manage.py migrate
    python manage.py runserver
    """

def browser():
    """
    1. Testar cada campo, deixando um não preenchido por vez, para ver se há, de fato, validação
    2. Testar todos preenchidos, para ver se há sucesso
    """
