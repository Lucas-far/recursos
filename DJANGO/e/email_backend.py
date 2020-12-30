

"""
Objetivo:
         imprimir formulários não modelo no terminal de um projeto
"""

def terminal():
    """
    pip install django==2.2.17 django-bootstrap4
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

def forms():
    """
    from django import forms
    from django.core.mail.message import EmailMessage

    class InterviewForm(forms.Form):

        choices_states = (
            ('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'),
            ('Bahia', 'Bahia'), ('Brasília', 'Brasília'), ('Ceará', 'Ceará'), ('Espírito Santo', 'Espírito Santo'),
            ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'),
            ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'),
            ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pará', 'Pará'), ('Pernambuco', 'Pernambuco'),
            ('Piauí', 'Piauí'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'),
            ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'),
            ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'),
            ('Tocantins', 'Tocantins')
        )

        choices_ny = (('não', 'não'), ('sim', 'sim'), ('talvez', 'talvez'))

        name = forms.CharField(label='Qual o seu nome?')
        email = forms.EmailField(label='Qual o seu e-mail?')
        state = forms.ChoiceField(label='Qual estado você mora?', choices=choices_states)
        foreign_country = forms.CharField(label='Qual país(es) deseja conhecer?')
        departure = forms.ChoiceField(label='Você deseja morar fora do Brasil?', choices=choices_ny)

        def print_data_into_terminal(self):
            content = \
                f'''
                ===================
                Dados da entrevista
                ===================

                Nome                             = {self.cleaned_data['name']}
                Email                            = {self.cleaned_data['email']}
                Estado em que reside             = {self.cleaned_data['state']}
                Países estrangeiros para visitar = {self.cleaned_data['foreign_country']}
                Deseja sair do Brasil?           = {self.cleaned_data['departure']}
                '''

            database = EmailMessage(
                body=content,
                headers={'Reply-To': self.cleaned_data['email']},
                subject='Respostas do Questionário sobre o Brasil',
                to=('meu_email@domínio.com',),
                from_email='meu_email@domínio.com'
            )
            database.send()
    """

def views():
    """
    class InterviewFormFormView(FormView):
        template_name = 'index.html'
        form_class = InterviewForm
        success_url = reverse_lazy('index')

        def form_valid(self, form, *args, **kwargs):
            form.print_data_into_terminal()
            messages.success(self.request, 'Seus dados foram enviados. Obrigado por participar!')
            return super(InterviewFormFormView, self).form_valid(form, *args, **kwargs)

        def form_invalid(self, form, *args, **kwargs):
            messages.error(self.request, 'Há erro em um ou mais campos do formulário!')
            return super(InterviewFormFormView, self).form_invalid(form, *args, **kwargs)
    """

def pa_urls():
    """
    from django.urls import path
    from .views import InterviewFormFormView
    urlpatterns = [path('formulario/', InterviewFormFormView.as_view(), name='formulario')]
    """

def templates():
    """
    <!DOCTYPE html>
    {% load bootstrap4 %}
    {% load static %}
    <html lang="en">
    <head>
        {% bootstrap_css %}
        <link href="#" rel="stylesheet">
        <meta charset="UTF-8">
        <meta content="ie-edge" http-equiv="X-UA-Compatible">
        <meta content="width=device-width, initial-scale=1, shrink-to-fit=no" name="viewport">
        <title>Página</title>
    </head>
    <style>
        .ma {margin: auto;}
    </style>
    <body>
        <div class="container">
                <form autocomplete="off" class="form" id="this-form" method="post">
                    {% csrf_token %}
                    {% bootstrap_messages %}
                    <fieldset><legend class="text-center">Formulário</legend></fieldset>
                    <div class="row">
                        <div class="col-6 col-sm-6 col-md-6 col-lg-6 col-xl-6 ma mb-2">
                            {% bootstrap_form form %}
                            {% buttons %}
                                <div class="text-center">
                                    <button class="btn btn-dark" form="this-form" type="submit">Enviar</button>
                                </div>
                            {% endbuttons %}
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

"Se for desejado, além de imprimir, também salvar os dados"

def models():
    """
    from django.db import models

    class Interview(models.Model):
        choices_states = (
            ('Acre', 'Acre'), ('Alagoas', 'Alagoas'), ('Amapá', 'Amapá'), ('Amazonas', 'Amazonas'),
            ('Bahia', 'Bahia'), ('Brasília', 'Brasília'), ('Ceará', 'Ceará'), ('Espírito Santo', 'Espírito Santo'),
            ('Goiás', 'Goiás'), ('Maranhão', 'Maranhão'), ('Mato Grosso', 'Mato Grosso'),
            ('Mato Grosso do Sul', 'Mato Grosso do Sul'), ('Minas Gerais', 'Minas Gerais'),
            ('Paraíba', 'Paraíba'), ('Paraná', 'Paraná'), ('Pará', 'Pará'), ('Pernambuco', 'Pernambuco'),
            ('Piauí', 'Piauí'), ('Rio de Janeiro', 'Rio de Janeiro'), ('Rio Grande do Norte', 'Rio Grande do Norte'),
            ('Rio Grande do Sul', 'Rio Grande do Sul'), ('Rondônia', 'Rondônia'), ('Roraima', 'Roraima'),
            ('Santa Catarina', 'Santa Catarina'), ('São Paulo', 'São Paulo'), ('Sergipe', 'Sergipe'),
            ('Tocantins', 'Tocantins')
        )

        choices_ny = (('não', 'não'), ('sim', 'sim'), ('talvez', 'talvez'))

        name = models.CharField('Qual o seu nome?', max_length=200)
        email = models.EmailField('Qual o seu e-mail?', max_length=200)
        state = models.CharField('Qual estado você mora?', choices=choices_states, max_length=19)
        foreign_country = models.CharField('Qual país(es) deseja conhecer?', max_length=1000)
        departure = models.CharField('Você deseja morar fora do Brasil?', choices=choices_ny, max_length=6)

        def __str__(self):
            return self.email

        class Meta:
            verbose_name = 'Entrevistado'
            verbose_name_plural = 'Entrevistados'
    """

def admin():
    """
    from django.contrib import admin
    from .models import Interview

    @admin.register(Interview)
    class InterViewAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'state', 'foreign_country', 'departure')
    """

# Adiciona-se a função que imprime, o adicional de criar um objeto
def forms2():
    """
    new = Interview.objects.create(
        name=self.cleaned_data['name'],
        email=self.cleaned_data['email'],
        state=self.cleaned_data['state'],
        foreign_country=self.cleaned_data['foreign_country'],
        departure=self.cleaned_data['departure']
    )
    new.save()
    """

# Verificar através do super usuário, se, ao preencher e enviar o formulário, há a impressão e criação dos dados
def terminal3():
    """ python manage.py createsuperuser """
