

"""
Módulo >>> widget.py

Objetivo:
         não sei informar

Objetivo alternativo:
                     converter um campo de formulário, que não recebe campo de texto diretamente, para receber
"""

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

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def views():
    """
    from django.contrib import messages
    from django.urls import reverse_lazy
    from django.views.generic import FormView
    from django.views.generic import TemplateView
    from .forms import *

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'

    class WidgetFormView(FormView):
        template_name = 'form.html'
        form_class = WidgetForm
        success_url = reverse_lazy('index')

        def form_valid(self, form, *args, **kwargs):
            form.print_into_terminal()
            messages.success(self.request, _('Sua mensagem foi enviada. Obrigado!'))
            return super(WidgetFormView, self).form_valid(form, *args, **kwargs)

        def form_invalid(self, form, *args, **kwargs):
            messages.error(self.request, _('Há algum erro no seu formulário!'))
            return super(WidgetFormView, self).form_invalid(form, *args, **kwargs)
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [
        path('', IndexTemplateView.as_view(), name='index'),
        path('form/', WidgetFormView.as_view(), name='form/')
        ]
    """

def forms():
    """
    from django import forms
    from django.core.mail.message import EmailMessage

    class WidgetForm(forms.Form):
        email = forms.EmailField(label='Email', min_length=2, max_length=150)
        commentary = forms.CharField(label='Seu comentário', widget=forms.Textarea())

        def print_into_terminal(self):
            content = f'Seu comentário\n{self.cleaned_data["commentary"]}'
            data_display = EmailMessage(
                body=content,
                headers={'Reply-To': self.cleaned_data['email']},
                subject='Comentário do usuário',
                to=('meu-email@domínio.com',),
                from_email='meu-email@domínio.com'
            )
            data_display.send()
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
    </head>
    <body>
        <div class="container text-center">
            {% bootstrap_messages %}
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# form.html (forma 1) (usando Django) (responsável por renderizar o campo que recebeu widget)
def templates2():
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
        <title>Página de formulário</title>
        <style>
            body {background-color: #222; color: white;}
            .ma {margin: auto;}
        </style>
    </head>
    <body>
        <div class="container mt-3">
            <form action="{% url 'form/' %}" class="form" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <h2 class="mt-2 text-center text-dark">Formulário</h2>
                <h6 class="text-center text-primary">Dê sua opinião</h6>
                <div class="row mt-5">
                    <div class="form-group ma">
                        {% bootstrap_form form %}
                    </div>
                </div>
                <div class="container mt-2 text-center">
                    <button class="btn btn-dark text-danger" form="this-form" type="submit">Enviar</button>
                </div>
            </form>
        </div>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

# form.html (forma 2) (usando bootstrap)
def templates3():
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
        <title>Página de formulário</title>
        <style>
            body {background-color: #222; color: white;}
            .ma {margin: auto;}
        </style>
    </head>
    <body>
        <div class="container mt-3">
            <form action="{% url 'form/' %}" class="form" id="this-form" method="post">
                {% csrf_token %}
                {% bootstrap_messages %}
                <h2 class="mt-2 text-center text-dark">Formulário</h2>
                <h6 class="text-primary text-center">Dê sua opinião</h6>
                <div class="row mt-5">
                    <div class="form-group ma">
                        <input class="form-control" min="2" max="150" name="email" size="40" placeholder="seu e-mail" type="email">
                    </div>
                </div>
                <div class="row mt-2">
                    <div class="form-group ma">
                        <input class="form-control" min="2" max="150" name="commentary" size="40" placeholder="seu comentário" type="text">
                    </div>
                </div>
                <div class="container mt-2 text-center">
                    <button class="btn btn-dark text-danger" form="this-form" type="submit">Enviar</button>
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
