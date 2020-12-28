

""" /home/lucas/PycharmProjects/model.objects.order_by('').all() """

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
    TEMPLATES = 'DIRS': ['templates']
    """

def pp_urls():
    """
    from django.urls import include
    urlpatterns = [path('', include('pa.urls'))]
    """

def models():
    """
    from django.db import models

    class Modelo(models.Model):
        texto = models.CharField('Texto', max_length=500)

        class Meta:
            verbose_name = 'Texto'
            verbose_name_plural = 'Textos'

        def __str__(self):
            return self.texto
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Modelo)
    class ModeloAdmin(admin.ModelAdmin):
        list_display = ('texto',)
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    """

def views():
    """
    from django.views.generic import TemplateView
    from .models import Modelo

    class IndexTemplateView(TemplateView):
        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super(IndexTemplateView, self).get_context_data(**kwargs)
            context['modelo'] = Modelo.objects.order_by('?').all()
            return context
    """

def pa_urls():
    """
    from django.urls import path
    from .views import *

    urlpatterns = [path('', IndexTemplateView.as_view(), name='index')]
    """

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
        {% for objeto in modelo %}
            <p>{{ objeto }}</p>
        {% endfor %}
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def terminal3():
    """
    python manage.py createsuperuser
    python manage.py runserver
    """

def template_admin():
    """
    1. criar pelo menos 2 objetos do bdd criado
    2. ir ao template índice e atualizar, para saber se o método surte efeito
    """
