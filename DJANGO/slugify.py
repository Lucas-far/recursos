

"""
Módulo >>> slugify.py

Objetivo:
         configurar slugify para criar slug de um campo de um modelo

Observação:
           slugify é dependente de outro método: signals
"""

def terminal():
    """
    pip install django==2.2.17
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """ INSTALLED_APPS = ['pa'] """

def models():
    """
    from django.db import models
    from django.db.models import signals
    from django.template.defaultfilters import slugify

    class Livro(models.Model):
        nome = models.CharField('Nome', max_length=150)
        pags = models.IntegerField('Número de páginas')
        slug = models.SlugField('Slug', blank=True, editable=False, max_length=200)

        class Meta:
            verbose_name = 'Livro'
            verbose_name_plural = 'Livros'

        def __str__(self):
            return self.nome

    def slugify_modelo_livro(instance, **kwargs):
        instance.slug = slugify(instance.nome)

    signals.pre_save.connect(slugify_modelo_livro, sender=Livro)
    """

def admin():
    """
    from django.contrib import admin
    from .models import *

    @admin.register(Livro)
    class LivroAdmin(admin.ModelAdmin):
        list_display = ('nome', 'pags', 'slug')
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

"Ir ao template admin e criar algum objeto, para certificar de que o slug do objeto foi executado"
