

"""
Módulo >>> economizar_dados_template.py

Objetivo:
         diminuir dados em um template combinando modelo com loop for
Fonte:
      /home/lucas/PycharmProjects/economizar_dados_template
"""

def terminal():
    """
    pip install django==2.2.17 django-bootstrap4 django-stdimage
    pip freeze > requirements.txt
    django-admin startproject pp .
    django-admin startapp pa
    """

def settings():
    """
    INSTALLED_APPS = ['pa', 'bootstrap4']
    TEMPLATES = [{'DIRS': ['templates']}]
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    """

def pp_urls():
    """
    from django.urls import include
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns = [path('', include('pa.urls'))] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """

def models():
    """
    from django.db import models
    from stdimage import StdImageField

    class Model(models.Model):
        text = models.TextField('Texto')
        avatar = StdImageField(
            upload_to='database_Model',
            variations={'Thumb': {'height': 500, 'width': 500, 'crop': True}}
        )

        def __str__(self):
            return self.text

        class Meta:
            verbose_name = 'Texto'
            verbose_name_plural = 'Textos'
    """

def admin():
    """
    from django.contrib import admin
    from .models import Model

    @admin.register(Model)
    class ModelAdmin(admin.ModelAdmin):
        list_display = ('text', 'avatar')
    """

def views():
    """
    from django.views.generic import ListView
    from .models import Model

    class IndexListView(ListView):
        model = Model
        template_name = 'index.html'
        context_object_name = 'queryset'
    """

def pa_urls():
    """
    from django.urls import path
    from .views import IndexListView
    urlpatterns = [path('', IndexListView.as_view(), name='index')]
    """

# Template vazio, para adicionar dados posteriormente
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
    <body>
    {% bootstrap_javascript jquery='full' %}
    </body>
    </html>
    """

def terminal2():
    """
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    """

"Ir ao template admin e criar objetos"

# Inserção dos objetos do bdd no template anteriormente criado
"Se não houvesse os dados salvos em um bdd, teriam que ser escritos diretamente no template"
def templates2():
    """
    <div class="container mt-5">
        {% for object in queryset %}
            <div class="row">
                <div class="col-6 border border-secondary text-center">
                    <img alt="" class="mt-4" src="{{ object.avatar.Thumb.url }}">
                </div>
                <div class="col-6 border border-primary">
                    <span>{{ object.text }}</span>
                </div>
            </div>
        {% endfor %}
    </div>
    """
