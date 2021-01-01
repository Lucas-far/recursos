

"""
Módulo >>> model_mommy.py

Objetivo:
         criar objetos de bancos de dados de forma mais dinâmica, assim como para usá-los em testes
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

# Configurando model_mommy
def terminal3():
    """
    pip install model_mommy
    pip freeze > requirements.txt
    python manage.py createsuperuser || para verificar, no template admin, se model_mommy funciona
    python manage.py runserver
    """

# Usando model_mommy
def terminal4():
    """
    python manage.py shell                       || abrir numa segunda janela de terminal
    from model_mommy import mommy                || importação
    var = mommy.make('NomeDoBdd')                || criação de um objeto
    var = mommy.make('NomeDoBdd', _quantity=int) || criação de múltiplos objetos
    var.campo                                    || chamada de um campo do objeto
    var.campo = novo valor                       || mudar valor de um campo do objeto
    var.save()                                   || salvar valor alterado em um objeto

    ALGORITMO de exemplo:

        index = 0
        while index < len(var):
            print(var[index].campo, '\n', var[index].campo2, '\n', var[index].campo3)
            index += 1
    """
