

# TODO -> Configurar [ from django.template.defaultfilters import slugify ]

def terminal():
    """
    pip install django
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

def browser():
    """
    1. http://127.0.0.1:8000/admin/
    2. cria-se um objeto do modelo, para verificar se o método slugify() terá êxito
    """
