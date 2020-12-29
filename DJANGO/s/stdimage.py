

"""
Objetivo:
         configurar imagens de um bdd para mostrar no template

Fonte:
      /home/lucas/PycharmProjects/show_image_from_database
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

    class Modelo(models.Model):
        nome = models.CharField('Nome completo', max_length=200)
        avatar = StdImageField(
            upload_to='database_Modelo',
            variations={'Thumb': {'height': 500, 'width': 500, 'crop': True}}
        )

        def __str__(self):
            return self.nome

        class Meta:
            verbose_name = 'Pessoa'
            verbose_name_plural = 'Pessoas'
    """

def admin():
    """
    from django.contrib import admin
    from .models import Modelo

    @admin.register(Modelo)
    class ModeloAdmin(admin.ModelAdmin):
        list_display = ('nome', 'avatar')
    """

def views():
    """
    from django.views.generic import ListView
    from django.urls import reverse_lazy
    from .models import Modelo

    class DatabaseListView(ListView):
        template_name = 'index.html'
        model = Modelo
        context_object_name = 'queryset'
        success_url = reverse_lazy('index')
    """

def pa_urls():
    """
    from django.urls import path
    from .views import DatabaseListView
    urlpatterns = [path('', DatabaseListView.as_view(), name='index')]
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
    <body>
        <table class="table table-dark table-bordered">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Avatar</th>
                </tr>
            </thead>
            <tbody>
            {% for index in queryset %}
                <tr>
                    <td>{{ index.nome }}</td>
                    <td>
                        <img src="{{ index.avatar.Thumb.url }}" alt="{{ index.nome }}">
                    </td>
                </tr>
            {% endfor %}
            </tbody>
            <tfoot></tfoot>
        </table>
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
